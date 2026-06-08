"""Маршруты для работы с конфигурацией."""

from fastapi import APIRouter, Depends

from app.dependencies import get_app_config, get_runtime_config_service
from app.schemas.app_config import AppConfigModel
from app.schemas.responses import HealthResponse, RuntimeConfigUpdateResponse
from app.schemas.runtime_config import RuntimeConfigModel, RuntimeConfigUpdateModel
from app.services.runtime_config_service import RuntimeConfigService

router = APIRouter(tags=["configuration"])


@router.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    """Проверка работоспособности приложения."""
    return HealthResponse(status="ok")


@router.get("/config/app", response_model=AppConfigModel)
async def get_static_config(
    app_config: AppConfigModel = Depends(get_app_config),
) -> AppConfigModel:
    """Получение статической конфигурации приложения.
    
    Статическая конфигурация не может быть изменена через API.
    """
    return app_config


@router.get("/config/runtime", response_model=RuntimeConfigModel)
async def get_runtime_config(
    service: RuntimeConfigService = Depends(get_runtime_config_service),
) -> RuntimeConfigModel:
    """Получение текущих runtime-настроек."""
    return service.get_config()


@router.put("/config/runtime", response_model=RuntimeConfigUpdateResponse)
async def update_runtime_config(
    new_config: RuntimeConfigUpdateModel,
    service: RuntimeConfigService = Depends(get_runtime_config_service),
) -> RuntimeConfigUpdateResponse:
    """Обновление runtime-настроек.
    
    Принимает JSON с новыми значениями параметров.
    Валидация выполняется автоматически через Pydantic.
    """
    updated = service.update_config(new_config)
    return RuntimeConfigUpdateResponse(
        message="Runtime-конфигурация обновлена",
        config=updated,
    )