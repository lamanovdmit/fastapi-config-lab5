"""Сервис для управления runtime-конфигурацией."""

from app.schemas.runtime_config import RuntimeConfigModel, RuntimeConfigUpdateModel


class RuntimeConfigService:
    """Сервис для хранения и обновления runtime-настроек."""

    def __init__(self, initial_config: RuntimeConfigModel):
        self._config = initial_config.model_copy(deep=True)

    def get_config(self) -> RuntimeConfigModel:
        """Возвращает текущие runtime-настройки."""
        return self._config

    def update_config(self, new_config: RuntimeConfigUpdateModel) -> RuntimeConfigModel:
        """Обновляет runtime-настройки.
        
        Args:
            new_config: Pydantic-модель с новыми значениями.
            
        Returns:
            Обновлённая модель runtime-настроек.
        """
        self._config = RuntimeConfigModel(**new_config.model_dump())
        return self._config