# config.py

import os
import pathlib
from functools import lru_cache
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
# we need to load the env file because it contains the GOOGLE_APPLICATION_CREDENTIALS
import firebase_admin

load_dotenv()

class Settings(BaseSettings):
    """Main settings"""
    app_name: str = "QRSmart"
    env: str = os.getenv("ENV", "development")
    # Needed for CORS
    frontend_url: str = os.getenv("FRONTEND_URL", "NA")

@lru_cache
def get_settings() -> Settings:
    """Retrieves the fastapi settings"""
    return Settings()

def get_firebase_app():
    """
        Initialize firebase
    """
    return firebase_admin.initialize_app()
