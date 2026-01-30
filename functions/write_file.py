def write_file(working_directory, file_path, content):
     try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        valid_target_dir = os.path.commonpath([abs_working_dir, abs_file_path]) == abs_working_dir
        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if not os.path.isdir(abs_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'