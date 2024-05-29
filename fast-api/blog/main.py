from fastapi import FastAPI, Depends
import uvicorn
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog')
def create(request: schemas.blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/blog")
def fetch(db: Session = Depends(get_db)):
    get_blog = db.query(models.Blog).all()
    return get_blog


@app.get(f"/blog/{id}")
def fetch_one(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).all()
    return blog


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
