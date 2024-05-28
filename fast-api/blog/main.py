from fastapi import FastAPI
import uvicorn
from . import schemas, models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post('/blog')
def create(request: schemas.blog):
    return request.title


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
