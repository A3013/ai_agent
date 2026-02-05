def run_python_file(working_directory, file_path, args=None):
    import subprocess
    import sys
    import os

    # Ensure the working directory exists
    if not os.path.isdir(working_directory):
        raise FileNotFoundError(f"Working directory '{working_directory}' does not exist.")

    # Ensure the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File '{file_path}' does not exist.")

    # Prepare the command to run the Python file
    command = [sys.executable, file_path]
    
    # Add any additional arguments if provided
    if args:
        command.extend(args)

    # Run the command in the specified working directory
    result = subprocess.run(command, cwd=working_directory, capture_output=True, text=True)

    # Check for errors and return output
    if result.returncode != 0:
        raise RuntimeError(f"Error running file: {result.stderr}")
    
    return result.stdout