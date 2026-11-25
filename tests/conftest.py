from random import randrange

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from database import tables
from src.generators.player import Player
from src.generators.user_type_generator import UserTypeBuilder


@pytest.fixture
def get_player_generator():
    """Создать генератор игрока с начальными значениями."""
    return Player()


@pytest.fixture
def get_user_type_generator():
    """Создать генератор случайных данных пользователя."""
    return UserTypeBuilder()


@pytest.fixture
def get_number():
    """Вернуть случайное число из диапазона от 1 до 996 с шагом пять."""
    return randrange(1, 1000, 5)


def _calculate(a, b):
    """Сложить два целых числа; для других типов вернуть None."""
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    return None


@pytest.fixture
def calculate():
    """Предоставить вспомогательную функцию сложения."""
    return _calculate


@pytest.fixture
def make_number():
    """Создать случайное число для параметризованных упражнений."""
    return randrange(1, 1000, 5)


@pytest.fixture
def get_database_session():
    """Выдать сессию к временной SQLite-базе, изолированной для теста."""
    test_engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    tables.Model.metadata.create_all(test_engine)
    test_session_factory = sessionmaker(bind=test_engine, autoflush=False, autocommit=False)
    session = test_session_factory()
    try:
        yield session
    finally:
        session.close()
        test_engine.dispose()


def delete_test_data(session, table, filter_data):
    """Удалить совпавшие записи в тестовой сессии и сохранить транзакцию."""
    session.query(table).filter(filter_data).delete()
    session.commit()


@pytest.fixture
def get_delete_method():
    """Предоставить вспомогательное удаление записей для тестовой базы."""
    return delete_test_data


def add_test_data(session, table, data):
    """Добавить запись в тестовую базу и вернуть её после сохранения."""
    obj = table(**data)
    session.add(obj)
    session.commit()
    return obj


@pytest.fixture
def get_data_add_method():
    """Предоставить вспомогательное добавление записей для тестовой базы."""
    return add_test_data
