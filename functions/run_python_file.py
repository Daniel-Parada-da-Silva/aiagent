import os
import subprocess

def run_python_file(working_directory, file_path):
    abs_workdir = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, file_path))

    if abs_target != abs_workdir and not abs_target.startswith(abs_workdir + os.sep):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_target):
        return f'Error: File "{file_path}" not found.'
    if not abs_target.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(["python3", os.path.basename(abs_target)], stderr=subprocess.PIPE, stdout=subprocess.PIPE, timeout=30, cwd = os.path.dirname(abs_target))

        out = result.stdout.decode()
        err = result.stderr.decode()

        lst = []
        if len(out.strip()) > 0:
            lst.append(f"STDOUT: {out}")
        if len(err.strip()) > 0:
            lst.append(f"STDERR: {err}")
        if len(lst) == 0:
            lst.append("No output produced.")
        if result.returncode != 0:
            lst.append(f"Process exited with code {result.returncode}")
        
        return "\n".join(lst)
    except Exception as e:
        return f"Error: executing Python file: {e}"