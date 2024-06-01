from fastapi import APIRouter, Depends, status, Response, HTTPException
import uvicorn
from .. import schemas, models, hash_p
from ..database import engine, get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.get("/", status_code=status.HTTP_201_CREATED, response_model=List[schemas.show_blog])
def fetch(db: Session = Depends(get_db)):
    get_blog = db.query(models.Blog).all()

    return get_blog

# if i use .first i will get one object , if i used .all() i will get one object inside a list except if i have many rows with same id


@router.get(f"/{id}", status_code=201, response_model=schemas.show_blog)
def fetch_one(id: int,  db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    return blog


# delete(synchronize_session=False)
@router.delete(f"/{id}")
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="blog not avabile ")
    blog.delete(
        synchronize_session=False)
    db.commit()
    return "deleted"


@router.put(f"/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request: schemas.blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="blog not avabile ")
    blog.update(request.dict())
    db.commit()
    return "updated"
