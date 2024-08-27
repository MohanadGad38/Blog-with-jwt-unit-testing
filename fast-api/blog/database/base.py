from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import declarative_base, declared_attr


# class Base(AsyncAttrs):
#     id: int
#     __name__: str

#     # This allows all models to have a table name that is the lowercase version of the model name
#     @declared_attr
#     def __tablename__(cls) -> str:
#         return cls.__name__.lower()


# Base = declarative_base(cls=Base)
