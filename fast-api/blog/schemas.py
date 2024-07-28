from pydantic import BaseModel, EmailStr
from typing import Annotated, Union, Optional


class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    class Config():
        from_attributes = True


class AddBlog(BlogBase):
    userid: str

    class Config():
        from_attributes = True


class User(BaseModel):
    name: str
    email: EmailStr
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: list[Blog] = []

    class Config:
        from_attributes = True


class ShowUserNameAndEmail(BaseModel):
    name: str
    email: str

    class Config:
        from_attributes = True


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUserNameAndEmail

    class Config():
        from_attributes = True


ShowUser.update_forward_refs()


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None
