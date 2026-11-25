"""Настройка SQLAlchemy для таблиц проекта."""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Model(DeclarativeBase):
    """Базовый класс ORM-моделей пользователей и заказов."""


# Укажите реальный URL через переменную окружения, если нужен PostgreSQL.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")
engine_options = {"connect_args": {"check_same_thread": False}} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, **engine_options)

# Создавайте отдельную сессию для каждой операции с базой данных.
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
