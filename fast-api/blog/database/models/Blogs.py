from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from blog.database.session import Base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base


class Blog(Base):
    __tablename__ = 'Blogs'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str]
    body: Mapped[str]
    test: Mapped[str]
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('Users.id'))
    creator: Mapped['Users'] = relationship("Users", back_populates="blogs")
# create index for title
