from blog.core.config import Settings
from functools import lru_cache
from sqlalchemy.orm import declarative_base


@lru_cache
def get_settings() -> Settings:
    return Settings(env_file='.env')


@lru_cache
def get_base() -> declarative_base:
    Base: declarative_base = declarative_base()
    return Base


settings: Settings = get_settings()
base: declarative_base = get_base()
