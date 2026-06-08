"""Точка входа FastAPI приложения."""

from fastapi import FastAPI

from .config import app_config
from .routes.config_routes import router as config_router

app = FastAPI(
    title=app_config.app_name,
    version=app_config.app_version,
    description=app_config.app_description,
    contact={
        "name": app_config.app_authors[0] if app_config.app_authors else "Author",
        "email": app_config.contact_email,
    },
    license_info={
        "name": app_config.license_name,
    },
)

app.include_router(config_router)