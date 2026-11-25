from random import randrange
import pytest

from src.generators import player_loc
from src.generators.player import Player


@pytest.fixture
def get_player_generator():
    return Player()


@pytest.fixture
def get_number():
    return randrange(1, 1000, 5)


def _calculate(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return None





@pytest.fixture
def calculate():
    return _calculate





@pytest.fixture
def make_number():
    print('i am getting number')
    number = randrange(1, 1000, 5)
    yield number
    print(f'number at home {number}')
