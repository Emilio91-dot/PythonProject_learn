class BuilderBaseClass:
    """Базовый класс для пошагового создания вложенных словарей."""

    def __init__(self):
        """Создать пустой словарь, который будет наполнять билдер."""
        self.result = {}

    def update_inner_value(self, keys, value):
        """Записать значение по ключу или по списку вложенных ключей.

        Список ["профиль", "имя"] создаёт или обновляет result["профиль"]["имя"].
        Возвращает билдер, чтобы вызовы можно было объединять в цепочку.
        """
        if not isinstance(keys, list):
            self.result[keys] = value
            return self
        if not keys:
            raise ValueError("keys must contain at least one item")

        current = self.result
        for key in keys[:-1]:
            child = current.setdefault(key, {})
            if not isinstance(child, dict):
                raise ValueError(f"Cannot descend through non-dictionary value at {key!r}")
            current = child
        current[keys[-1]] = value
        return self

    def build(self):
        """Вернуть копию словаря с собранными данными."""
        return self.result.copy()
