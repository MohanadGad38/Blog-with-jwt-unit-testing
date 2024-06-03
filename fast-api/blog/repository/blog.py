from fastapi import Depends, status, HTTPException
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List


def get_all(db: Session = Depends(get_db)):
    get_blog: models.Blog = db.query(models.Blog).all()
    return get_blog


def create(request: schemas.addblog, db: Session = Depends(get_db)):
    new_blog: models.Blog = models.Blog(
        title=request.title, body=request.body, user_id=request.userid)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete(id: int, db: Session = Depends(get_db)):
    blog: models.Blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="blog not avabile ")
    blog.delete(
        synchronize_session=False)
    db.commit()
    return "deleted"


def update(request: schemas.blog, id: int, db: Session = Depends(get_db)):
    blog: models.Blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="blog not avabile ")
    blog.update(request.dict())
    db.commit()
    return "updated"


def get_one(id: int, db: Session = Depends(get_db)):
    blog: models.Blog = db.query(models.Blog).filter(
        models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    return blog
