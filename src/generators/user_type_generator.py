from src.baseclasses.builder import BuilderBaseClass

from faker import Faker
from decimal import Decimal
import random

fake = Faker("ru_RU")



class UserTypeBuilder:

    def __init__(self):
        self.reset()

    def reset(self):
        self.result = {
            "name": fake.user_name(),
            "email": fake.email(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "age": random.randint(18, 60),
            "phone": fake.phone_number(),
            "city": fake.city(),
            "country": "Россия",
            "registration_date": fake.date_time_this_year(),
            "is_active": random.choice([True, False]),
            "balance": round(random.uniform(0, 100000), 2),
            "status": random.choice(
                ["ACTIVE", "INACTIVE", "BANNED"]
            )
        }

        return self

    def build(self):
        return self.result.copy()