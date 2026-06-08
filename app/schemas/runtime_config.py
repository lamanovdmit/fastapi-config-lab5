"""Pydantic-модели для runtime-конфигурации."""

from enum import Enum
from pydantic import BaseModel, Field


class LogLevel(str, Enum):
    """Допустимые уровни логирования."""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class RuntimeConfigModel(BaseModel):
    """Модель runtime-настроек для ответа API."""

    log_level: LogLevel = Field(default=LogLevel.INFO, description="Уровень логирования")
    feature_flag: bool = Field(default=True, description="Флаг функциональности")
    maintenance_mode: bool = Field(default=False, description="Режим обслуживания")
    runtime_message: str = Field(
        default="Приложение работает в штатном режиме",
        description="Сообщение runtime-режима",
    )


class RuntimeConfigUpdateModel(BaseModel):
    """Модель для обновления runtime-настроек (тело запроса)."""

    log_level: LogLevel = Field(default=LogLevel.INFO, description="Уровень логирования")
    feature_flag: bool = Field(default=True, description="Флаг функциональности")
    maintenance_mode: bool = Field(default=False, description="Режим обслуживания")
    runtime_message: str = Field(
        default="Приложение работает в штатном режиме",
        description="Сообщение runtime-режима",
    )