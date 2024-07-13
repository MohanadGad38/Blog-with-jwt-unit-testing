from pydantic import BaseModel, EmailStr
from typing import Annotated, Union, Optional


class blogbase(BaseModel):
    title: str
    body: str


class blog(blogbase):
    class Config():
        from_attributes = True


class addblog(blogbase):
    userid: str

    class Config():
        from_attributes = True


class user(BaseModel):
    name: str
    email: EmailStr
    password: str


class show_user(BaseModel):
    name: str
    email: str
    blogs: list[blog] = []

    class Config:
        from_attributes = True


class ShowUserNameAndEmail(BaseModel):
    name: str
    email: str

    class Config:
        from_attributes = True


class show_blog(BaseModel):
    title: str
    body: str
    creator: ShowUserNameAndEmail

    class Config():
        from_attributes = True


show_user.update_forward_refs()


class login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None
