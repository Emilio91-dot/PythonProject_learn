from src.baseclasses.pyenam import PyEnam


class Genders(PyEnam):
    """Допустимые значения пола пользователя из API."""

    FEMALE = "female"
    MALE = "male"


class Statuses(PyEnam):
    """Статусы учётной записи, используемые моделями и генераторами."""

    ACTIVE = "active"
    INACTIVE = "inactive"
    BANNED = "banned"
    DELETED = "deleted"
    MEMBER = "member"

    @classmethod
    def _missing_(cls, value):
        """Принимать строковые статусы без учёта регистра."""
        if isinstance(value, str):
            normalized = value.lower()
            for status in cls:
                if status.value == normalized:
                    return status
        return None


class UserErrors(PyEnam):
    """Текстовые сообщения об ошибках валидации пользователя."""

    WRONG_EMAIL = "Invalid email address."
