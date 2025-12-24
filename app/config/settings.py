# app/config/settings.py

import os
from pathlib import Path

# Project base directory
BASE_DIR = Path(__file__).resolve().parent.parent


class Settings:
    APP_NAME: str = "Product Catalog Service"
    APP_VERSION: str = "1.0.0"

    # Database
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: str = os.getenv("DB_PORT", "5432")
    DB_NAME: str = os.getenv("DB_NAME", "products_db")
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "pg123456")

    DATABASE_URL: str = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


settings = Settings()
