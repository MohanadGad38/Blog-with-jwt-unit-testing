from typing import Any
from sqlalchemy import create_engine
from sqlalchemy.engine.interfaces import Dialect
from sqlalchemy.engine.mock import MockConnection
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase, Mapped, mapped_column
import os
from dotenv import load_dotenv

load_dotenv()
SQLALCHAMY_DATABASE_URL = os.getenv('DATABASE_URL')
engine: AsyncEngine = create_async_engine(SQLALCHAMY_DATABASE_URL, future=True,
                                          echo=True,)
SessionLocal = async_sessionmaker(engine)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


async def create_database_if_not_exists():
    async with engine.begin() as conn:
        # Create the database if it does not exist
        await conn.run_sync(Base.metadata.create_all)


async def get_db():
    await create_database_if_not_exists()
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
