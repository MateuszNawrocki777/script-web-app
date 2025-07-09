from fastapi import FastAPI
import subprocess

from access_functions import (get_scripts_by_username, has_access_to_script,
                              get_script_file_by_id)

app = FastAPI()


@app.get("/scripts")
def get_my_scripts():
    return get_scripts_by_username("Example")


@app.post("/run/{script_id}")
def run_script(script_id):
    script_id = int(script_id)
    if has_access_to_script("Example", script_id):
        subprocess.call(["/bin/sh", get_script_file_by_id(script_id)])
