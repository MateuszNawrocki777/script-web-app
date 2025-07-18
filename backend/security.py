from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

from passlib.context import CryptContext
import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta, timezone

from access_functions import get_user_by_username, exists_user_with_username


import os
from dotenv import load_dotenv

load_dotenv()


TOKEN_VALIDITY_MINUTES = 10
ALGORITHM = "HS256"
SECURITY_SECRET_KEY = os.getenv("SECURITY_SECRET_KEY")

AUTHORIZATION_EXCEPTION = HTTPException(
        status_code=403,
        detail="Invalid username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(BaseModel):
    username: str
    hashedPassword: str
    scriptIds: list[int]


class Token(BaseModel):
    access_token: str
    token_type: str


def get_username(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        data = jwt.decode(token, SECURITY_SECRET_KEY, algorithms=[ALGORITHM])
        username: str = data.get("sub")
        if username is None:
            raise AUTHORIZATION_EXCEPTION
        if not exists_user_with_username(username):
            raise AUTHORIZATION_EXCEPTION
        return username
    except InvalidTokenError:
        print("Invalid token")
        raise AUTHORIZATION_EXCEPTION


def login_function(data_form: Annotated[OAuth2PasswordRequestForm, Depends()]):
    username = data_form.username
    password = data_form.password

    user = get_user_by_username(username)
    if user is None:
        raise AUTHORIZATION_EXCEPTION
    if not check_password(user, password):
        raise AUTHORIZATION_EXCEPTION

    return generate_token(username)


def check_password(user: User, password: str):
    return pwd_context.verify(password, user["hashedPassword"])


def generate_token(username: str):
    expire = datetime.now(timezone.utc) + timedelta(TOKEN_VALIDITY_MINUTES)
    data = {
        "sub": username,
        "exp": expire
        }
    token = jwt.encode(data, SECURITY_SECRET_KEY, algorithm=ALGORITHM)

    return Token(
        access_token=token,
        token_type="bearer"
    )

# Example user has password "Example"
# to generate hashed password run:
# pwd_context.hash(password)
