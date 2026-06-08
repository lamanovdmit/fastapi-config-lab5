"""Маршруты для работы с конфигурацией."""

from fastapi import APIRouter, HTTPException

from ..config import app_config
from ..services.runtime_config_service import runtime_service

router = APIRouter()


@router.get("/health")
async def health_check():
    """Проверка работоспособности приложения."""
    return {"status": "ok"}


@router.get("/config/app")
async def get_static_config():
    """Получение статической конфигурации приложения."""
    return app_config.to_dict()


@router.get("/config/runtime")
async def get_runtime_config():
    """Получение текущих runtime-настроек."""
    return runtime_service.get_config()


@router.put("/config/runtime")
async def update_runtime_config(new_config: dict):
    """Обновление runtime-настроек."""
    try:
        updated_config = runtime_service.update_config(new_config)
        return {
            "message": "Runtime-конфигурация обновлена",
            "config": updated_config,
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))