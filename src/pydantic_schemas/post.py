from pydantic import BaseModel, Field, field_validator


class Post(BaseModel):
    """Модель публикации с дополнительным ограничением для учебного ID."""

    id: int
    title: str
    name: str | None = Field(default=None, alias="_name")

    @field_validator("id")
    @classmethod
    def check_that_id_is_less_than_two(cls, value):
        """Не принимать ID больше двух в этом примере валидации."""
        if value > 2:
            raise ValueError("ID must be less than 2")
        return value
