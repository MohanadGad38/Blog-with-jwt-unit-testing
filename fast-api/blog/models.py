from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from blog.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Blog(Base):
    __tablename__ = 'Blogs'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str]
    body: Mapped[str]
    test: Mapped[str]
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('Users.id'))
    creator: Mapped['Users'] = relationship("Users", back_populates="blogs")


class Users(Base):
    __tablename__ = 'Users'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str]
    blogs: Mapped[list[Blog]] = relationship("Blog", back_populates="creator")
