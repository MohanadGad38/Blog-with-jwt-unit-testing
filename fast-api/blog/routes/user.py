from fastapi import APIRouter, Depends, status, Response, HTTPException
import uvicorn
import schemas
import models
import hash_p
from database import engine, get_db
from sqlalchemy.orm import Session
from typing import List
from repository import user
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
router = APIRouter(
    prefix="/user",
    tags=['Users']
)


@router.post("/")
def create_user(request: schemas.user, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get(f"/{id}", status_code=201)
async def get_user(id: int, db: AsyncSession = Depends(get_db)):
    gg = await user.get(id, db)
    print(gg)
    return gg
