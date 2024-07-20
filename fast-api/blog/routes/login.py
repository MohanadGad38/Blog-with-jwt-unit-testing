from fastapi import Depends, status, HTTPException, APIRouter
from blog import schemas
from blog import models
from blog import hash_p
from blog import JWTToken
from blog.database import get_db
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import create_engine, Column, Integer, String, select

router = APIRouter(
    prefix="/login",
    tags=['Login']
)


@router.post('/')
async def login(request: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)) -> dict[str, str]:
    user_query: models.Users = select(models.Users).where(
        models.Users.email == request.username)
    result = await db.execute(user_query)
    user = result.scalar_one_or_none()
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
