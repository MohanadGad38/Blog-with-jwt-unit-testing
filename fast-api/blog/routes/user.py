from fastapi import APIRouter, Depends, status, Response, HTTPException
import uvicorn
from .. import schemas, models, hash_p
from ..database import engine, get_db
from sqlalchemy.orm import Session
from typing import List
router = APIRouter(
    prefix="/user",
    tags=['Users']
)


@router.post("/")
def create_user(request: schemas.user, db: Session = Depends(get_db)):
    new_user = models.Users(
        name=request.name, email=request.email,
        password=hash_p.hashing.create_hash(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()
    return new_user


@router.get(f"/{id}", status_code=201, response_model=schemas.show_user)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user
