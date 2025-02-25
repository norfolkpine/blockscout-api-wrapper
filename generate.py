import subprocess
import sys
import os

def generate_python_client(swagger_yaml_path: str, output_dir: str):
    subprocess.run([
        sys.executable, "-m", "openapi_python_client",
        "generate",
        "--path", swagger_yaml_path,
        "--output-path", output_dir
    ])

if __name__ == "__main__":
    yaml_file = "swagger.yaml"  # path to your swagger YAML file
    output_directory = "blockscout_api_client"

    if not os.path.exists(yaml_file):
        print(f"YAML file '{yaml_file}' not found.")
    else:
        generate_python_client(yaml_file, output_directory)
        print(f"Client successfully generated in '{output_directory}/'")
