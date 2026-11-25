"""Генератор случайных данных пользователя для тестов."""

import random
from decimal import Decimal

from faker import Faker


class UserTypeBuilder:
    """Собирать реалистичные тестовые данные пользователя."""

    def __init__(self):
        """Создать Faker для русской локали и заполнить данные."""
        self.fake = Faker("ru_RU")
        self.reset()

    def reset(self):
        """Сгенерировать новый набор пользовательских данных."""
        self.result = {
            "name": self.fake.user_name(),
            "email": self.fake.email(),
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
            "age": random.randint(18, 60),
            "phone": self.fake.phone_number(),
            "city": self.fake.city(),
            "country": "Россия",
            "registration_date": self.fake.date_time_this_year(),
            "is_active": random.choice([True, False]),
            "balance": Decimal(f"{random.uniform(0, 100000):.2f}"),
            "status": random.choice(["ACTIVE", "INACTIVE", "BANNED"]),
        }
        return self

    def build(self):
        """Вернуть копию сгенерированного словаря пользователя."""
        return self.result.copy()
