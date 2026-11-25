from src.baseclasses.pyenam import PyEnam


class Genders(PyEnam):
    FEMALE = "female"
    MALE = "male"


class Statuses(PyEnam):
    ACTIVE = "active"
    INACTIVE = "inactive"
    BANNED = "banned"
    DELETED = "deleted"
    MEMBER = "member"

    @classmethod
    def _missing_(cls, value):
        if isinstance(value, str):
            normalized = value.lower()
            for status in cls:
                if status.value == normalized:
                    return status
        return None


class UserErrors(PyEnam):
    WRONG_EMAIL = "Invalid email address."
