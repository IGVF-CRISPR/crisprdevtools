import os
def create_new_module_nextflow(module_name):
  # Create directories
  os.makedirs(f"{module_name}/bin", exist_ok=True)
  os.makedirs(f"{module_name}/conda_envs", exist_ok=True)
  os.makedirs(f"{module_name}/example_data", exist_ok=True)
  os.makedirs(f"{module_name}/processes", exist_ok=True)
  os.makedirs(f"{module_name}/test", exist_ok=True)

  # Create files
  with open(f"{module_name}/README.md", "w") as f:
      pass

  with open(f"{module_name}/input.config", "w") as f:
      pass

  with open(f"{module_name}/main.nf", "w") as f:
      f.write("nextflow.enable.dsl=2\n")

  with open(f"{module_name}/bin/{module_name}.py", "w") as f:
      f.write("#!/usr/bin/env python\n")

  conda_file = f'''name: {module_name}
  channels:
    - conda-forge
    - bioconda
    - defaults
  dependencies:
    - numpy=1.23.5
    - pandas=2.2.1
    - pip
    - pip:
      - openpyxl==3.1.2
  '''

  with open(f"{module_name}/conda_envs/{module_name}.yaml", "w") as f:
      f.write(conda_file)


  process = f'''process seqSpecParser {{
    conda "${{moduleDir}}/conda_envs/{module_name}.yaml"
    input:
    output:
    script:
          """
          {module_name}.py
          """
  }}
  '''

  with open(f"{module_name}/processes/{module_name}.nf", "w") as f:
      f.write(process)


#create_new_module_nextflow('test')