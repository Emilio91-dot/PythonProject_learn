import pytest
import requests

from configuration import REQUEST_TIMEOUT, SERVICE_URL


@pytest.fixture
def get_users():
    """Получить список пользователей с ограничением времени ожидания."""
    return requests.get(SERVICE_URL, timeout=REQUEST_TIMEOUT)
