from pydantic import BaseModel, HttpUrl, UUID4
from pydantic.color import Color


class Physical(BaseModel):
    """Модель физических характеристик устройства."""

    color: Color
    photo: HttpUrl
    uuid: UUID4
