import pytest

from src.baseclasses.builder import BuilderBaseClass


def test_builder_sets_a_top_level_value():
    """Проверяет, что билдер записывает значение в корень словаря."""
    builder = BuilderBaseClass()

    assert builder.update_inner_value("name", "Ada").build() == {"name": "Ada"}


def test_builder_sets_a_nested_value_and_returns_itself():
    """Проверяет создание вложенного значения и возврат того же билдера."""
    builder = BuilderBaseClass()

    result = builder.update_inner_value(["profile", "locale"], "ru_RU")

    assert result is builder
    assert builder.build() == {"profile": {"locale": "ru_RU"}}


def test_builder_keeps_sibling_nested_values():
    """Проверяет, что добавление соседнего ключа сохраняет уже записанное значение."""
    builder = BuilderBaseClass()
    builder.update_inner_value(["profile", "name"], "Ada")
    builder.update_inner_value(["profile", "locale"], "en_US")

    assert builder.build() == {"profile": {"name": "Ada", "locale": "en_US"}}


def test_builder_rejects_an_empty_path():
    """Проверяет, что пустой путь заканчивается понятной ошибкой."""
    with pytest.raises(ValueError, match="at least one item"):
        BuilderBaseClass().update_inner_value([], "value")


def test_builder_rejects_a_path_through_a_scalar():
    """Проверяет, что билдер не пытается пройти внутрь обычного значения."""
    builder = BuilderBaseClass().update_inner_value("profile", "not a dictionary")

    with pytest.raises(ValueError, match="non-dictionary"):
        builder.update_inner_value(["profile", "locale"], "ru_RU")
