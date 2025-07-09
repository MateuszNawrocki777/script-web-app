from fastapi import FastAPI

from access_functions import get_scripts_by_username

app = FastAPI()


@app.get("/scripts")
def get_my_scripts():
    return get_scripts_by_username("Example")
