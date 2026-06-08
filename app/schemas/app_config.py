"""Pydantic-модель статической конфигурации приложения."""

from pydantic import BaseModel, Field


class AppConfigModel(BaseModel):
    """Статическая конфигурация приложения.
    
    Не может быть изменена через API.
    Изменения применяются только после перезапуска сервера.
    """

    app_name: str = Field(..., description="Название приложения")
    app_version: str = Field(..., description="Версия приложения")
    app_description: str = Field(..., description="Описание приложения")
    app_authors: list[str] = Field(..., description="Список авторов")
    contact_email: str = Field(..., description="Контактный email")
    license_name: str = Field(..., description="Тип лицензии")