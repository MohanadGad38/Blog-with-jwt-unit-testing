from pydantic import BaseModel


class blog(BaseModel):
    title: str
    body: str
