def test_get_number_returns_fixture_value(get_number):
    """Проверяет, что фикстура возвращает целое число из настроенного диапазона."""
    assert isinstance(get_number, int)
    assert 1 <= get_number < 1000
    assert get_number % 5 == 1
