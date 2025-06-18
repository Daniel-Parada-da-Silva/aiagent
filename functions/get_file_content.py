import os

def get_file_content(working_directory, file_path):
    abs_workdir = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, file_path))

    if abs_target != abs_workdir and not abs_target.startswith(abs_workdir + os.sep):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(abs_target):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        MAX_CHARS = 10000

        with open(abs_target, "r") as f:
            file_content_string = f.read(MAX_CHARS + 1)
            f.close()
        
        if len(file_content_string) > MAX_CHARS:
            file_content_string = file_content_string[:MAX_CHARS] + f'[...File "{file_path}" truncated at 10000 characters]'

        return file_content_string
    except Exception as error:
        return f"Error: {error}"
    