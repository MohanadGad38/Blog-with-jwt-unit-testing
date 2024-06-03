from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, FastAPI, HTTPException, status
from typing import Annotated, Union
from . import JWTToken

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return JWTToken.verfiy_token(token, credentials_exception)
    # # user = get_user(fake_users_db, username=token_data.username)
    # # if user is None:
    # #     raise credentials_exception
    # return "user"
