from enum import Enum

from src.baseclasses.pyenam import PyEnam

class Genders(Enum):
    female = "female"
    male = "male"



class Statuses(PyEnam):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    BANNED = "BANNED"
    DELETED = "DELETED"
    MEMBER = "MEMBER"


class UserErrors(Enum):
    WRONG_EMAIL = "wrong_email"


print(Statuses.list())