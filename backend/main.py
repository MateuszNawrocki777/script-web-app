from fastapi import FastAPI

from dataloader import load_scripts, load_users

app = FastAPI()

SCRIPTS = load_scripts()
USERS = load_users()


@app.get("/scripts")
def read_root():
    return SCRIPTS
