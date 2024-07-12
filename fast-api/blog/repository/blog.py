from fastapi import Depends, status, HTTPException
import schemas
import models
from database import get_db
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from typing import List
from sqlalchemy.orm import Session, selectinload, joinedload
from sqlalchemy import create_engine, Column, Integer, String, select
from typing import Tuple, Optional, Dict, Any


async def get_all(db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(models.Blog).options(joinedload(models.Blog.creator))
    )
    blogs = result.scalars().all()
    return blogs


async def create(request: schemas.addblog, db: AsyncSession = Depends(get_db)):
    new_blog: models.Blog = models.Blog(
        title=request.title, body=request.body, user_id=request.userid)
    db.add(new_blog)
    try:
        await db.commit()
        await db.refresh(new_blog)
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        db.close
    return new_blog


async def delete(id: int, db: AsyncSession = Depends(get_db)):
    async with db.begin():
        blog_query = select(models.Blog).where(models.Blog.id == id)
        result = await db.execute(blog_query)
        blog = result.scalar_one_or_none()

        if not blog:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")

        db.delete(blog)
        await db.commit()

    return {"message": "Blog deleted successfully"}


def update(request: schemas.blog, id: int, db: Session = Depends(get_db)):
    blog: models.Blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="blog not avabile ")
    blog.update(request.dict())
    db.commit()
    return "updated"


async def get_one(id: int, db: AsyncSession = Depends(get_db)) -> Any | schemas.show_blog | None:
    statement: models.Blog = select(models.Blog).options(
        joinedload(models.Blog.creator)).where(models.Blog.id == id)
    result = await db.execute(statement)
    blog: schemas.show_blog = result.scalar_one_or_none()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    return blog
