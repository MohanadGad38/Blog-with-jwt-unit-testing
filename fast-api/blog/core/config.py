from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn, HttpUrl
import json
import json
import logging
import logging.config
from fastapi import FastAPI, Request
import logging
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
import time


class Settings(BaseSettings):
    """
    to config any settings in applications
    """
    DATABASE_URL: str
    model_config = SettingsConfigDict(
        env_file='.env', extra='ignore')
