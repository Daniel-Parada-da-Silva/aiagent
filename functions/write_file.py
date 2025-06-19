import os

from google.genai import types

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
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Creates a new file with the content. If the file already exists, overwrites the content of a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description=f"File path, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description=f"Content to write into the file"
            )
        },
    ),
)