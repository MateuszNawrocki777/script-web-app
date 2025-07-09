from fastapi import FastAPI
import subprocess

from dataloader import load_scripts

app = FastAPI()

SCRIPTS = load_scripts()


@app.get("/")
def read_root():
    subprocess.call(["/bin/sh", SCRIPTS[0]["file"]])
    return SCRIPTS
