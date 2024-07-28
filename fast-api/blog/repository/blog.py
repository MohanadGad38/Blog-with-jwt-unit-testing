from fastapi import Depends, status, HTTPException
from blog import schemas
from blog import models
from blog.database import get_db
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


async def create(request: schemas.AddBlog, db: AsyncSession = Depends(get_db)):
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


async def update(request: schemas.Blog, id: int, db: AsyncSession = Depends(get_db)):
    result = select(models.Blog).where(models.Blog.id == id)
    query_result = await db.execute(result)
    blog = query_result.scalar_one_or_none()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")

    # Update the blog attributes
    blog.title = request.title
    blog.body = request.body

    # Commit the changes
    await db.commit()

    return {"message": "Blog updated successfully"}


async def get_one(id: int, db: AsyncSession = Depends(get_db)) -> Any | schemas.ShowBlog | None:
    statement: models.Blog = select(models.Blog).options(
        joinedload(models.Blog.creator)).where(models.Blog.id == id)
    result = await db.execute(statement)
    blog: schemas.show_blog = result.scalar_one_or_none()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    return blog
