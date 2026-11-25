import pytest

from examples import computer
from src.enamc.user_enums import Statuses
from src.generators.player_loc import PlayerLoc
from src.schemas.computer import Computer


@pytest.mark.parametrize("status", Statuses.list())
def test_player_generator_sets_status(status, get_player_generator):
    result = get_player_generator.set_status(status).build()
    assert result["account_status"] == status


@pytest.mark.parametrize("balance", [100, 0, -10, "100"])
def test_player_generator_sets_balance(balance, get_player_generator):
    result = get_player_generator.set_balance(balance).build()
    assert result["balance"] == balance


def test_player_generator_starts_with_expected_fields(get_player_generator):
    result = get_player_generator.build()
    assert set(result) == {"account_status", "balance", "avatar", "localize"}
    assert {"en", "ru"} <= result["localize"].keys()


def test_player_generator_updates_nested_localization(get_player_generator):
    result = get_player_generator.update_inner_value(
        ["localize", "fr"], PlayerLoc("fr_FR").set_number(15).build()
    ).build()
    assert result["localize"]["fr"]["number"] == 15


def test_computer_example_matches_schema():
    result = Computer.model_validate(computer)
    assert result.id == computer["id"]
