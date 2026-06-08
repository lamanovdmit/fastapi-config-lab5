"""Функции-провайдеры зависимостей для FastAPI."""

from fastapi import Request

from app.schemas.app_config import AppConfigModel
from app.services.runtime_config_service import RuntimeConfigService


def get_app_config(request: Request) -> AppConfigModel:
    """Возвращает статическую конфигурацию приложения."""
    return request.app.state.dependencies["app_config"]


def get_runtime_config_service(request: Request) -> RuntimeConfigService:
    """Возвращает сервис runtime-конфигурации."""
    return request.app.state.dependencies["runtime_config_service"]