import pytest
import requests

from configuration import REQUEST_TIMEOUT, SERVICE_URL


@pytest.fixture
def get_users():
    return requests.get(SERVICE_URL, timeout=REQUEST_TIMEOUT)
