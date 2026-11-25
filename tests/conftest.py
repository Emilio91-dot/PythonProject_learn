from random import randrange

import pytest

from src.generators.player import Player


@pytest.fixture
def get_player_generator():
    """Создать генератор игрока с начальными значениями."""
    return Player()


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
