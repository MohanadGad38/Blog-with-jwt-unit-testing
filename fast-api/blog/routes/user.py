from fastapi import APIRouter, Depends, status, Response, HTTPException
import uvicorn
from blog import schemas
from blog import oauth2
from blog import models
from blog import hash_p
from blog.database import engine, get_db
from sqlalchemy.orm import Session
from typing import List
from blog.repository import user
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
router = APIRouter(
    prefix="/user",
    tags=['Users']
)


@router.post("/")
async def create_user(request: schemas.user, db: AsyncSession = Depends(get_db)):
    return await user.create(request, db)


@router.get(f"/{id}", status_code=201, response_model=schemas.ShowUserNameAndEmail)
async def get_user(id: int, db: AsyncSession = Depends(get_db), get_current_user: schemas.user = Depends(oauth2.get_current_user)) -> user.Dict[str, str] | None:
    return await user.get(id, db)
