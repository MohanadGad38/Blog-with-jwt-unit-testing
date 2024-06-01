from pydantic import BaseModel


class blogbase(BaseModel):
    title: str
    body: str


class blog(blogbase):
    class Config():
        orm_mode = True


class user(BaseModel):
    name: str
    email: str
    password: str


class show_user(BaseModel):
    name: str
    email: str
    blogs: list[blog] = []

    class Config():
        orm_mode = True


class show_blog(BaseModel):
    title: str
    body: str
    creator: show_user

    class Config():
        orm_mode = True
