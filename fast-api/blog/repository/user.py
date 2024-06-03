from fastapi import Depends, status, HTTPException
from .. import schemas, models, hash_p
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List


def create(request: schemas.user, db: Session = Depends(get_db)):
    new_user: models.Users = models.Users(
        name=request.name, email=request.email,
        password=hash_p.hashing.create_hash(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()
    return new_user


def get(id: int, db: Session = Depends(get_db)):
    # add types please
    user: models.Users = db.query(models.Users).filter(
        models.Users.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user
