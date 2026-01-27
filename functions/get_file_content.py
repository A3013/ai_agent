MAX_CHARS = 10000
import os

def get_file_content(working_directory, file_path):
    valid_target_dir = os.path.commonpath([working_directory, file_path]) == working_directory
    if not valid_target_dir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'