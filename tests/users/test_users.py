import pytest

from examples import computer
from src.enamc.user_enums import Statuses
from src.generators.player_loc import PlayerLoc
from src.schemas.computer import Computer
from database import tables


@pytest.mark.parametrize("status", Statuses.list())
def test_player_generator_sets_status(status, get_player_generator):
    """Проверяет, что генератор записывает каждый допустимый статус."""
    assert get_player_generator.set_status(status).build()["account_status"] == status


@pytest.mark.parametrize("balance", [100, 0, -10, "100"])
def test_player_generator_sets_balance(balance, get_player_generator):
    """Проверяет, что генератор сохраняет переданное значение баланса."""
    assert get_player_generator.set_balance(balance).build()["balance"] == balance


def test_player_generator_updates_nested_localization(get_player_generator):
    """Проверяет добавление локализованных данных во вложенный словарь игрока."""
    result = get_player_generator.update_inner_value(
        ["localize", "fr"], PlayerLoc("fr_FR").set_number(15).build()
    ).build()
    assert result["localize"]["fr"]["number"] == 15


def test_computer_example_matches_schema():
    """Проверяет, что учебный пример компьютера проходит Pydantic-валидацию."""
    result = Computer.model_validate(computer)
    assert result.id == computer["id"]


def test_get_data_users_uses_isolated_test_database(get_database_session, get_user_type_generator):
    """Проверяет чтение пользователя из отдельной временной SQLite-базы."""
    get_database_session.add(tables.Users(id=1, **get_user_type_generator.build()))
    get_database_session.commit()

    user = get_database_session.query(tables.Users).first()

    assert user is not None
    assert user.id == 1


def test_delete_helper_removes_only_matching_test_records(
    get_database_session, get_delete_method, get_user_type_generator
):
    """Проверяет удаление выбранной записи только из временной тестовой базы."""
    get_database_session.add(tables.Users(id=3, **get_user_type_generator.build()))
    get_database_session.add(tables.Users(id=4, **get_user_type_generator.build()))
    get_database_session.commit()

    get_delete_method(get_database_session, tables.Users, tables.Users.id == 3)

    assert get_database_session.query(tables.Users).filter_by(id=3).first() is None
    assert get_database_session.query(tables.Users).filter_by(id=4).first() is not None


def test_user_type_generator_data_can_be_saved_and_removed(
    get_database_session, get_data_add_method, get_user_type_generator
):
    """Проверяет, что тестовый пользователь сохраняется и удаляется без задержек."""
    user = get_data_add_method(
        get_database_session,
        tables.Users,
        get_user_type_generator.build(),
    )

    assert user.id is not None

    get_database_session.delete(user)
    get_database_session.commit()
    assert get_database_session.query(tables.Users).filter_by(id=user.id).first() is None
