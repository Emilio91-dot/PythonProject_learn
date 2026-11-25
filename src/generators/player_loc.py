from faker import Faker


class PlayerLoc:
    """Создавать локализованные тестовые данные игрока."""

    def __init__(self, lang):
        """Выбрать локаль Faker и сгенерировать имя для профиля."""
        self.fake = Faker(lang)
        self.result = {"nickname": self.fake.first_name()}

    def set_number(self, number=11):
        """Добавить номер в словарь локализованных данных."""
        self.result["number"] = number
        return self

    def build(self):
        """Вернуть копию собранных локализованных данных."""
        return self.result.copy()
