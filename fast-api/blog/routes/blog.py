from fastapi import APIRouter, Depends, status
from blog.schemas import blog_schema
from blog.schemas import blog_user_shared
from blog.schemas import user_schema
from blog import oauth2
from blog.database.session import get_db
from blog.database.models import Blog_model
from sqlalchemy.orm import Session
from typing import List
from blog.repository import blog
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from typing import Tuple, Optional, Dict, Any
router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create(request: blog_schema.AddBlog, db: AsyncSession = Depends(get_db), get_current_user: user_schema.User = Depends(oauth2.get_current_user)) -> blog_schema.Blog:
    return await blog.create(request, db)


@router.get("/", status_code=status.HTTP_201_CREATED, response_model=List[blog_user_shared.ShowBlog])
async def fetch(db: AsyncSession = Depends(get_db), get_current_user: user_schema.User = Depends(oauth2.get_current_user)):
    return await blog.get_all(db)

# if i use .first i will get one object , if i used .all() i will get one object inside a list except if i have many rows with same id


@ router.get(f"/{id}", status_code=201, response_model=blog_user_shared.ShowBlog)
async def fetch_one(id: int,  db: AsyncSession = Depends(get_db), get_current_user: user_schema.User = Depends(oauth2.get_current_user)) -> Any | blog_user_shared.ShowBlog | None:
    return await blog.get_one(id, db)


# delete(synchronize_session=False)
@ router.delete(f"/{id}")
async def delete_blog(id: int, db: AsyncSession = Depends(get_db), get_current_user: user_schema.User = Depends(oauth2.get_current_user)):
    return await blog.delete(id, db)


@ router.put(f"/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_blog(id: int, request: blog_schema.Blog, db: AsyncSession = Depends(get_db), get_current_user: user_schema.User = Depends(oauth2.get_current_user)):
    return await blog.update(request, id, db)
