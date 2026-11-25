from enum import Enum


class PyEnam(Enum):
    """Перечисление с общим методом получения списка значений."""

    @classmethod
    def list(cls):
        """Вернуть значения всех элементов перечисления."""
        return [item.value for item in cls]
