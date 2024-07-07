from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase, Mapped, mapped_column


class Blog(Base):
    __tablename__ = 'Blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('Users.id'))
    creator = relationship("Users", back_populates="blogs")


class Users(Base):
    __tablename__ = 'Users'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str]
    blogs: Mapped[list[Blog]] = relationship("Blog", back_populates="creator")
