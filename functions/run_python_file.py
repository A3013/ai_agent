import subprocess
import sys
import os


def run_python_file(working_directory, file_path, args=None):
    
    try:
        # Ensure the working directory exists
        if not os.path.isdir(working_directory):
            raise FileNotFoundError(f"Working directory '{working_directory}' does not exist.")

        #ensuring the file path is within the working directory
        working_dir_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.abspath(file_path)
        valid_file_path = os.path.commonpath([working_dir_abs, file_path_abs]) == working_dir_abs
        if not valid_file_path:
            raise f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        

        # Ensure the file exists
        if not os.path.isfile(file_path):
            raise f'Error: "{file_path}" does not exist or is not a regular file'

        #ensure the file has a .py extension
        if not file_path.endswith('.py'):
            raise f'Error: "{file_path}" is not a Python file'

        # Prepare the command to run the Python file
        command = ["python", file_path_abs]
        
        # Add any additional arguments if provided
        if args:
            command.extend(args)

        # Run the command in the specified working directory
        result = subprocess.run(command, cwd=working_directory, capture_output=True, text=True, timeout=30)

        # Check for errors and return output
        if result.returncode != 0:
            raise f"Process exited with code {result.returncode}"
        if result.stderr == None or result.stdout == None:
            raise "No output produced"
        else:
            output_string = f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}"

        return output_string
    except Exception as e:
        return f"Error: executing Python file: {e}"