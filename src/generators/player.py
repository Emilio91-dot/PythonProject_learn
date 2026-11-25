from src.baseclasses.builder import BuilderBaseClass
from src.enamc.user_enums import Statuses
from src.generators.player_loc import PlayerLoc


class Player(BuilderBaseClass):
    """Собирать словарь тестового игрока с локализованными данными."""

    def __init__(self):
        """Создать генератор и заполнить его значениями по умолчанию."""
        super().__init__()
        self.reset()

    def set_status(self, status=Statuses.ACTIVE.value):
        """Установить статус учётной записи."""
        self.result["account_status"] = status
        return self

    def set_balance(self, balance=0):
        """Установить баланс игрока."""
        self.result["balance"] = balance
        return self

    def set_avatar(self, avatar="https://www.google.com/"):
        """Установить адрес изображения профиля."""
        self.result["avatar"] = avatar
        return self

    def reset(self):
        """Восстановить поля по умолчанию и создать локализации en и ru."""
        self.result = {}
        self.set_status()
        self.set_avatar()
        self.set_balance()
        self.result["localize"] = {
            "en": PlayerLoc("en_US").build(),
            "ru": PlayerLoc("ru_RU").build(),
        }
        return self
