"""Сервис для управления runtime-конфигурацией."""

from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class RuntimeConfig:
    """Runtime-настройки, которые можно менять во время работы приложения."""

    log_level: str = "INFO"
    feature_flag: bool = True
    maintenance_mode: bool = False
    runtime_message: str = "Приложение работает в штатном режиме"


class RuntimeConfigService:
    """Singleton-сервис для хранения и обновления runtime-настроек."""

    _instance: Optional["RuntimeConfigService"] = None
    _config: RuntimeConfig

    def __new__(cls) -> "RuntimeConfigService":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._config = RuntimeConfig()
        return cls._instance

    def get_config(self) -> dict:
        """Возвращает текущие runtime-настройки."""
        return asdict(self._config)

    def update_config(self, new_values: dict) -> dict:
        """Обновляет runtime-настройки."""
        for key, value in new_values.items():
            if hasattr(self._config, key):
                setattr(self._config, key, value)
        return self.get_config()


runtime_service = RuntimeConfigService()