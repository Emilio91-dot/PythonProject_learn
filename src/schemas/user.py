from pydantic import BaseModel, EmailStr

from src.enamc.user_enums import Genders, Statuses


class User(BaseModel):
    """Проверяемая модель пользователя внешнего API."""

    id: int
    name: str
    email: EmailStr
    gender: Genders
    status: Statuses
