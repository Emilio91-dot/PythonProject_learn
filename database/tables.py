# from dns.serial import Serial
# from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
#
# from database_1 import Model

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
    Numeric
)

from database.database_1 import Model


class Users(Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    first_name = Column(String)
    last_name = Column(String)

    age = Column(Integer)
    phone = Column(String)

    city = Column(String)
    country = Column(String)

    registration_date = Column(DateTime)

    is_active = Column(Boolean)

    balance = Column(Numeric)

    status = Column(String)


class Orders(Model):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)

    product = Column(String)

    amount = Column(Integer)

    user_id = Column(Integer, ForeignKey('users.id'))


    # name
    # email
    # first_name
    # last_name
    # age
    # phone
    # city
    # country
    # registration_date
    # is_active
    # balance
    # status