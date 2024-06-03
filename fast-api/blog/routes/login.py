from fastapi import Depends, status, HTTPException, APIRouter
from .. import schemas, models, hash_p, JWTToken
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/login",
    tags=['Login']
)


@router.post('/')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user: models.Users = db.query(models.Users).filter(
        models.Users.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='wrong tyep')
    if not hash_p.hashing.verfiy(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='wrong password')

    user.id = "sumary_line"
    access_token_expires = timedelta(minutes=30)
    access_token = JWTToken.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
