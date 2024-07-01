from fastapi import Depends, status, HTTPException
import schemas
import models
import hash_p
from database import get_db
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import create_engine, Column, Integer, String, select


def create(request: schemas.user, db: AsyncSession = Depends(get_db)):
    new_user: models.Users = models.Users(
        name=request.name, email=request.email,
        password=hash_p.hashing.create_hash(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()
    return new_user


async def get(id: int, db: AsyncSession = Depends(get_db)):
    # add types please
    statement = select(models.Users).where(models.Users.id == id)
    result = await db.execute(statement)
    # print("dfdsdmskdn")
    # print(result.scalars().one())

    # user: models.Users = db.query(models.Users).filter(
    #     models.Users.id == id).first()
    # print(user)
    # if not user:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    # return await 'result'
    # results = await db.execute(select(models.Users))
    # users = results.scalars().all()
    gg = result.scalars().one_or_none()
    return gg
