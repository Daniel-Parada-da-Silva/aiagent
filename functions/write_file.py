import os

def write_file(working_directory, file_path, content):
    abs_workdir = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, file_path))

    if abs_target != abs_workdir and not abs_target.startswith(abs_workdir + os.sep):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        if not os.path.exists(abs_target):
            dire = os.sep.join(abs_target.split(os.sep)[:-1])
            os.makedirs(dire, mode=755, exist_ok=True)
        with open(abs_target, "w+") as f:
            f.write(content)
            f.close()
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as error:
        return f"Error: {error}"