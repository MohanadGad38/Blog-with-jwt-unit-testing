from pydantic import BaseModel, EmailStr
from typing import Annotated, Union, Optional
from blog.schemas.blog_schema import Blog
from blog.schemas.user_schema import ShowUserNameAndEmail


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: list[Blog] = []

    class Config:
        from_attributes = True


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUserNameAndEmail

    class Config:
        from_attributes = True
