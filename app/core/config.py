from functools import lru_cache
from pydantic import BaseSettings
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    app_name: str = "VectorShift Backend"
    debug: bool = True
    cors_allow_origins: List[str] = [os.getenv("FRONTEND_URL")]

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings() -> Settings:
    return Settings()