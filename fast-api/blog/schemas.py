from pydantic import BaseModel


class blog(BaseModel):
    title: str
    body: str


class show_blog(blog):
    class Config():
        orm_mode = True


class user(BaseModel):
    name: str
    email: str
    password: str
