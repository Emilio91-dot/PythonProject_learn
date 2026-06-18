from random import randrange
import pytest

from src.generators import player_loc
from src.generators.player import Player


from src.generators.user_type_generator import UserTypeBuilder


from database.database_1 import SessionLocal



@pytest.fixture
def get_player_generator():
    return Player()


@pytest.fixture
def get_user_type_generator():
    return UserTypeBuilder()


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


@pytest.fixture
def get_database_session():
   session = SessionLocal()
   try:
       yield session
   finally:
       session.close()


def delete_test_data(session, table, filter_data):
    session.query(table).filter(filter_data).delete()
    session.commit()





@pytest.fixture
def get_delete_method():
    return delete_test_data


def add_test_data(session, table, data):
    obj = table(**data)
    session.add(obj)
    session.commit()
    return obj


@pytest.fixture
def get_data_add_method():
    return add_test_data
