"""Настройка SQLAlchemy и фабрика сессий базы данных."""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Model(DeclarativeBase):
    """Базовый класс для ORM-моделей проекта."""


# Строку подключения можно переопределить через переменную окружения.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")

# SQLite в режиме многопоточности требует отдельного параметра подключения.
engine_options = {"connect_args": {"check_same_thread": False}} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, **engine_options)

# Фабрика создаёт сессии без неявной отправки изменений в базу.
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
