from fastapi import FastAPI
import uvicorn
from . import models
from .database import engine
from .routes import blog, user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(blog.router)
app.include_router(user.router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
