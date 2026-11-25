from enum import Enum


class GlobalErrorMessage(Enum):
    WRONG_STATUS_CODE = "Received status code does not match the expected value."
    WRONG_ELEMENT_COUNT = "The number of items does not match the expected value."
