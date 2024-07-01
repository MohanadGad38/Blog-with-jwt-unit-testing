from typing import Any
from sqlalchemy import create_engine
from sqlalchemy.engine.interfaces import Dialect
from sqlalchemy.engine.mock import MockConnection
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase, Mapped, mapped_column


SQLALCHAMY_DATABASE_URL = "sqlite+aiosqlite:///blog.db"
engine: AsyncEngine = create_async_engine(SQLALCHAMY_DATABASE_URL, connect_args={
    "check_same_thread": False})
SessionLocal = async_sessionmaker(engine)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


async def get_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
