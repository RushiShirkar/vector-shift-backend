from functools import lru_cache
from pydantic_settings import BaseSettings
from pydantic import Extra
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    app_name: str = "VectorShift Backend"
    debug: bool = True
    cors_allow_origins: List[str] = ["*"]

    class Config:
        env_file = ".env"
        extra = Extra.allow

@lru_cache()
def get_settings() -> Settings:
    return Settings()