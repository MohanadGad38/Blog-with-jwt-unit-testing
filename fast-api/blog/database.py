from sqlalchemy import create_engine

SQLALCHAMY_DATABASE_URL = "sqlite://./blog.db"
engine = create_engine(SQLALCHAMY_DATABASE_URL)
