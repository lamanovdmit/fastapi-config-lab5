"""Статическая конфигурация приложения."""

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class AppConfig:
    """Кастомный класс статической конфигурации приложения.
    
    Атрибут frozen=True делает класс неизменяемым после создания.
    Изменение параметров возможно только после перезапуска сервера.
    """

    app_name: str
    app_version: str
    app_description: str
    app_authors: List[str]
    contact_email: str
    license_name: str

    def to_dict(self) -> dict:
        """Возвращает конфигурацию в виде словаря."""
        return {
            "app_name": self.app_name,
            "app_version": self.app_version,
            "app_description": self.app_description,
            "app_authors": self.app_authors,
            "contact_email": self.contact_email,
            "license_name": self.license_name,
        }


app_config = AppConfig(
    app_name="Laboratory FastAPI App",
    app_version="1.0.0",
    app_description="Учебное приложение для лабораторной работы №5",
    app_authors=["Ламанов Дмитрий"],
    contact_email="lamanovdmit@gmail.com",
    license_name="MIT",
)