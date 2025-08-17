from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
import subprocess
from typing import Annotated

from security import get_username, login_function

from access_functions import (get_scripts_by_username, has_access_to_script,
                              get_script_file_by_id)

import os
from dotenv import load_dotenv

load_dotenv()
CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/scripts")
def get_my_scripts(username: Annotated[str, Depends(get_username)]):
    return get_scripts_by_username(username)


@app.post("/run/{script_id}")
def run_script(script_id, username: Annotated[str, Depends(get_username)]):
    script_id = int(script_id)
    if has_access_to_script(username, script_id):
        script_file = get_script_file_by_id(script_id)
        if script_file is None:
            raise HTTPException(
                status_code=402,
                detail="Script file not found"
            )
        subprocess.call(["/bin/sh", get_script_file_by_id(script_id)])
    else:
        raise HTTPException(
            status_code=403,
            detail="Unauthorized to run this script"
        )


@app.post("/login")
def login(data_form: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return login_function(data_form)
