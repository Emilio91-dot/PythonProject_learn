from pydantic import BaseModel, EmailStr, field_validator

from src.enamc.user_enums import Genders, Statuses, UserErrors


class User(BaseModel):
    id: int
    name: int
    email: str
    gender: Genders
    status: Statuses

    @field_validator("email")
    @classmethod
    def check_email(cls, email):
        if "@" not in email:
            raise ValueError(UserErrors.WRONG_EMAIL.value)
        return email

        @field_validator("email")
        @classmethod
        def validate_email(cls, email):
            if "test" in email:
                raise ValueError(UserErrors.WRONG_EMAIL.value)
            return v