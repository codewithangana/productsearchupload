# app/main.py

from fastapi import FastAPI

from app.config.settings import settings
from app.db.session import engine
from app.db.base import Base
from app.api.upload import router as upload_router
from app.api.products import router as products_router

# Create tables (for local/dev; Alembic preferred in prod)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

# Register routers
app.include_router(upload_router)
app.include_router(products_router)
