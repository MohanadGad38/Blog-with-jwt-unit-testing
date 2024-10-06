from pydantic import BaseModel, EmailStr
from typing import Annotated, Union, Optional


class User(BaseModel):
    name: str
    email: EmailStr
    password: str


class ShowUserNameAndEmail(BaseModel):
    name: str
    email: str

    class Config:
        from_attributes = True
