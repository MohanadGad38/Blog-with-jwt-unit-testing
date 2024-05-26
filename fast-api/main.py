from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def index():
    return 'heyy'


@app.get('/blogg')
def bloglimit(limit=10, pub: bool = True, sorts: Optional[str] = None):
    if pub:
        return {'data': f'{limit} published blogs from the db '}
    else:
        return {'data': f'{limit} blogs from db '}


@app.get('/blog/{id}')
def blog(id: int):
    return {"data": id}


class Blog(BaseModel):
    title: str
    body: str
    publish: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return {"data": f"Blog is created !! {request.title}"}
