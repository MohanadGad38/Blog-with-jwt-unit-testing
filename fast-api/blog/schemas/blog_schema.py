from pydantic import BaseModel
from blog.schemas import user_schema


class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    class Config:
        from_attributes = True


class AddBlog(BlogBase):
    userid: int

    class Config:
        from_attributes = True
