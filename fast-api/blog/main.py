from fastapi import FastAPI
import uvicorn
from blog.database.session import engine
from blog.routes import blog, user, login
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()
config = dotenv_values(".env")


app = FastAPI()
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(login.router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=90)
