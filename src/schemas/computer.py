from pydantic import BaseModel, EmailStr, FutureDate, HttpUrl, PastDate, PaymentCardNumber, UUID4
from pydantic.networks import IPv4Address, IPv6Address

from src.enamc.user_enums import Statuses
from src.schemas.pysical import Physical


class Owner(BaseModel):
    """Контактные данные владельца компьютера."""

    name: str
    card_number: PaymentCardNumber
    email: EmailStr


class DetailedInfo(BaseModel):
    """Сгруппированные сведения о внешнем виде и владельцах."""

    physical: Physical
    owners: list[Owner]


class Computer(BaseModel):
    """Проверяемая модель компьютера с сетевыми и временными полями."""

    id: int
    status: Statuses
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPv4Address
    host_v6: IPv6Address
    detailed_info: DetailedInfo
