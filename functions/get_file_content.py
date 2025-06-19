import os
from google.genai import types

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    abs_workdir = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, file_path))

    if abs_target != abs_workdir and not abs_target.startswith(abs_workdir + os.sep):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(abs_target):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        

        with open(abs_target, "r") as f:
            file_content_string = f.read(MAX_CHARS + 1)
            f.close()
        
        if len(file_content_string) > MAX_CHARS:
            file_content_string = file_content_string[:MAX_CHARS] + f'[...File "{file_path}" truncated at 10000 characters]'

        return file_content_string
    except Exception as error:
        return f"Error: {error}"
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Get the content of the specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description=f"File path, relative to the working directory.",
            ),
        },
    ),
)
    