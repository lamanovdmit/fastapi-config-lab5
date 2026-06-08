"""Pydantic-модели для ответов API."""

from pydantic import BaseModel, Field

from app.schemas.runtime_config import RuntimeConfigModel


class HealthResponse(BaseModel):
    """Ответ эндпоинта проверки работоспособности."""

    status: str = Field(default="ok", description="Статус приложения")


class RuntimeConfigUpdateResponse(BaseModel):
    """Ответ эндпоинта обновления runtime-конфигурации."""

    message: str = Field(..., description="Сообщение о результате операции")
    config: RuntimeConfigModel = Field(..., description="Обновлённая конфигурация")