from decimal import Decimal

from src.generators.user_type_generator import UserTypeBuilder


def test_user_type_builder_creates_all_user_fields():
    """Проверяет наличие полей, соответствующих ORM-модели пользователя."""
    user = UserTypeBuilder().build()

    assert set(user) == {
        "name", "email", "first_name", "last_name", "age", "phone",
        "city", "country", "registration_date", "is_active", "balance", "status",
    }


def test_user_type_builder_generates_values_with_expected_types():
    """Проверяет типы и диапазоны случайных пользовательских данных."""
    user = UserTypeBuilder().build()

    assert "@" in user["email"]
    assert 18 <= user["age"] <= 60
    assert isinstance(user["balance"], Decimal)
    assert user["balance"] >= 0
    assert user["status"] in {"ACTIVE", "INACTIVE", "BANNED"}


def test_user_type_builder_reset_generates_a_new_result_dictionary():
    """Проверяет, что reset создаёт новый словарь, сохраняя fluent-интерфейс."""
    builder = UserTypeBuilder()
    original = builder.build()

    assert builder.reset() is builder
    assert builder.build() is not original
