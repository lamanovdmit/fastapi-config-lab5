"""Точка входа FastAPI приложения с dependency injection."""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.init_dependencies import init_dependencies
from app.routes.config_routes import router as config_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Управляет жизненным циклом приложения.
    
    При старте создаёт словарь зависимостей.
    При завершении освобождает ресурсы.
    """
    deps = init_dependencies()
    app.state.dependencies = deps
    print("Dependencies initialized:", list(deps.keys()))
    yield
    print("App is shut down")


app = FastAPI(
    lifespan=lifespan,
    title="Laboratory FastAPI App",
    version="1.0.0",
    description="Учебное приложение для лабораторной работы №6",
)


@app.get("/")
async def get_root():
    """Перенаправляет корневой маршрут на документацию."""
    return RedirectResponse("/docs")


@app.get("/ping")
async def ping_server():
    """Проверка доступности сервера."""
    return "pong"


app.include_router(config_router)