"""Инициализация словаря зависимостей приложения."""

from app.schemas.app_config import AppConfigModel
from app.schemas.runtime_config import RuntimeConfigModel
from app.services.runtime_config_service import RuntimeConfigService


def init_dependencies() -> dict:
    """Создаёт и возвращает кастомный словарь зависимостей.
    
    Вызывается один раз при старте приложения (в lifespan).
    Содержит все сервисы и конфигурации, доступные через Depends.
    """
    app_config = AppConfigModel(
        app_name="Laboratory FastAPI App",
        app_version="1.0.0",
        app_description="Учебное приложение для лабораторной работы №6",
        app_authors=["Ламанов Дмитрий"],
        contact_email="lamanovdmit@gmail.com",
        license_name="MIT",
    )

    initial_runtime_config = RuntimeConfigModel(
        log_level="INFO",
        feature_flag=True,
        maintenance_mode=False,
        runtime_message="Приложение работает в штатном режиме",
    )

    runtime_service = RuntimeConfigService(initial_config=initial_runtime_config)

    return {
        "app_config": app_config,
        "runtime_config_service": runtime_service,
    }