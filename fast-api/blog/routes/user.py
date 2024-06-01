from fastapi import APIRouter, Depends, status, Response, HTTPException
import uvicorn
from .. import schemas, models, hash_p
from ..database import engine, get_db
from sqlalchemy.orm import Session
from typing import List
from ..repository import user
router = APIRouter(
    prefix="/user",
    tags=['Users']
)


@router.post("/")
def create_user(request: schemas.user, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get(f"/{id}", status_code=201, response_model=schemas.show_user)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get(id, db)
