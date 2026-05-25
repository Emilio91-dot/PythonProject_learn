from enum import Enum

class GlobalErrorMessage(Enum):
    WRONG_STATUS_CODE = "Received status code is not equel to expected."
    WRONG_ELEMENT_COUNT = "Number of items is not equal to expected."
