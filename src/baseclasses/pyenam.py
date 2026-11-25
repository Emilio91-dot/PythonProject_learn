from enum import Enum


class PyEnam(Enum):
    @classmethod
    def list(cls):
        return [item.value for item in cls]
