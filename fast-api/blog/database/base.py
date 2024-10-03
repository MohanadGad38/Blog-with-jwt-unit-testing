from blog.core.config import Settings
from functools import lru_cache


@lru_cache
def get_settings() -> Settings:
    return Settings(env_file='.env')


settings: Settings = get_settings()
