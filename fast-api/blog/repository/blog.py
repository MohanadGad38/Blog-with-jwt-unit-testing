from fastapi import Depends, status, HTTPException
import schemas
import models
from database import get_db
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from typing import List
from sqlalchemy.orm import Session, selectinload, joinedload
from sqlalchemy import create_engine, Column, Integer, String, select


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


def delete(id: int, db: Session = Depends(get_db)):
    blog: models.Blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="blog not avabile ")
    blog.delete(
        synchronize_session=False)
    db.commit()
    return "deleted"


def update(request: schemas.blog, id: int, db: Session = Depends(get_db)):
    blog: models.Blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="blog not avabile ")
    blog.update(request.dict())
    db.commit()
    return "updated"


def get_one(id: int, db: Session = Depends(get_db)):
    blog: models.Blog = db.query(models.Blog).filter(
        models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    return blog
