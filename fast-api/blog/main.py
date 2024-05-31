from fastapi import FastAPI, Depends, status, Response, HTTPException
import uvicorn
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schemas.blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/blog", status_code=status.HTTP_201_CREATED, response_model=List[schemas.show_blog])
def fetch(db: Session = Depends(get_db)):
    get_blog = db.query(models.Blog).all()

    return get_blog

# if i use .first i will get one object , if i used .all() i will get one object inside a list except if i have many rows with same id


@app.get(f"/blog/{id}", status_code=201, response_model=schemas.show_blog)
def fetch_one(id: int, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    return blog


# delete(synchronize_session=False)
@app.delete(f"/blog/{id}")
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="blog not avabile ")
    blog.delete(
        synchronize_session=False)
    db.commit()
    return "deleted"


@app.put(f"/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request: schemas.blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="blog not avabile ")
    blog.update(request.dict())
    db.commit()
    return "updated"


@app.post("/user")
def create_user(request: schemas.user, db: Session = Depends(get_db)):
    new_user = models.Users(
        name=request.name, email=request.email, password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()
    return request


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
