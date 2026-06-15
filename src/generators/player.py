

from src.baseclasses.builder import BuilderBaseClass


from src.enamc.user_enums import Statuses
from src.generators.player_loc import PlayerLoc

class Player(BuilderBaseClass):

    def __init__(self):
        super().__init__()
        self.reset()

    def set_status(self, status=Statuses.ACTIVE.value):
        self.result['account_status'] = status
        return self

    def set_balance(self, balance=0):
        self.result['balance'] = balance
        return self

    def set_avatar(self, avatar="https://www.google.com/"):
        self.result['avatar'] = avatar
        return self

    def reset(self):
        self.result = {}
        self.set_status()
        self.set_avatar()
        self.set_balance()
        self.result["localize"] = {
            "en": PlayerLoc('en_US').build(),
            "ru": PlayerLoc('ru_RU').build()
        }
        return self