from src.enamc.user_enums import Statuses
from src.generators.player import Player
from src.generators.player_loc import PlayerLoc


def test_player_has_the_default_fields_and_locales():
    player = Player().build()

    assert player["account_status"] == Statuses.ACTIVE.value
    assert player["balance"] == 0
    assert player["avatar"] == "https://www.google.com/"
    assert set(player["localize"]) == {"en", "ru"}
    assert player["localize"]["en"]["nickname"]
    assert player["localize"]["ru"]["nickname"]


def test_player_setters_can_be_chained():
    player = Player().set_status(Statuses.INACTIVE.value).set_balance(25).set_avatar("https://example.com/avatar.png")

    assert player.build()["account_status"] == Statuses.INACTIVE.value
    assert player.build()["balance"] == 25
    assert player.build()["avatar"] == "https://example.com/avatar.png"


def test_player_reset_restores_defaults():
    player = Player().set_balance(25).reset()

    assert player.build()["balance"] == 0
    assert player.build()["account_status"] == Statuses.ACTIVE.value


def test_player_localization_can_include_a_number():
    localization = PlayerLoc("en_US").set_number(11).build()

    assert localization["number"] == 11
    assert localization["nickname"]
