import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    abs_workdir = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, directory))

    if abs_target != abs_workdir and not abs_target.startswith(abs_workdir + os.sep):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_target):
        return f'Error: "{directory}" is not a directory'
    
    try:
        lst = []
        for name in os.listdir(abs_target):
            file = os.path.join(abs_target, name)
            size = os.path.getsize(file)
            is_dir = os.path.isdir(file)

            lst.append(f"- {name}: file_size={size}, is_dir={is_dir}")

        return "\n".join(lst)
    except Exception as error:
        return f"Error: {error}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
