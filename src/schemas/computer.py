
from pydantic import BaseModel, HttpUrl, UUID4, PaymentCardNumber, EmailStr

from pydantic import PastDate, FutureDate

from typing import List

from pydantic.networks import IPv4Address, IPv6Address
from src.enamc.user_enums import Statuses
from pydantic.color import Color
from src.schemas.pysical import Physical





class Owners(BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr



class DetailedInfo(BaseModel):
    physical: Physical
    owners: List[Owners]

class Computer(BaseModel):
    id: int
    status: Statuses
    activated_at: PastDate
    expiration_at : FutureDate
    host_v4: IPv4Address
    host_v6: IPv6Address
    detailed_info: DetailedInfo



# comp = Computer.model_validate(computer)
#
# print(comp)