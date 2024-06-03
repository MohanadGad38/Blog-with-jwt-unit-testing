from fastapi import APIRouter, Depends, status
from .. import schemas, oauth2
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.blog, db: Session = Depends(get_db)):
    return blog.create(request, db)


@router.get("/", status_code=status.HTTP_201_CREATED, response_model=List[schemas.show_blog])
def fetch(db: Session = Depends(get_db)):
    return blog.get_all(db)

# if i use .first i will get one object , if i used .all() i will get one object inside a list except if i have many rows with same id


@router.get(f"/{id}", status_code=201, response_model=schemas.show_blog)
def fetch_one(id: int,  db: Session = Depends(get_db)):
    return blog.get_one(id, db)


# delete(synchronize_session=False)
@router.delete(f"/{id}")
def delete_blog(id: int, db: Session = Depends(get_db)):
    return blog.delete(id, db)


@router.put(f"/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request: schemas.blog, db: Session = Depends(get_db)):
    return blog.update(request, id, db)
