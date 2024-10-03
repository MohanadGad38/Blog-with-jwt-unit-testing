from fastapi import APIRouter, Depends, status, Response, HTTPException
import uvicorn
from blog.schemas import user_schema, blog_schema, blog_user_shared
from blog import oauth2
from blog import hash_p
from blog.database.session import engine, get_db
from sqlalchemy.orm import Session
from typing import List
from blog.repository import user
from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
router = APIRouter(
    prefix="/user",
    tags=['Users']
)


@router.post("/")
async def create_user(request: user_schema.User, db: AsyncSession = Depends(get_db)):
    return await user.create(request, db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=blog_user_shared.ShowUserNameAndEmail)
async def get_user(id: int, db: AsyncSession = Depends(get_db),
                   get_current_user: user_schema.User = Depends(oauth2.get_current_user)) -> Optional[blog_user_shared.ShowUserNameAndEmail]:
    return await user.get(id, db)
