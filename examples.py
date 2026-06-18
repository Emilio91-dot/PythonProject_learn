
from database.database_1 import SessionLocal
from database import tables


def main():
    with SessionLocal() as session:
        users = (
            session.query(tables.Users)
            .filter(
                tables.Users.id.between(10, 50),
                tables.Users.age.between(20, 30)
            )
            .order_by(tables.Users.id.desc())
            .all()
        )

        for user in users:
            print({
                column.name: getattr(user, column.name)
                for column in user.__table__.columns
            })


if __name__ == "__main__":
    main()




# рабочий билд
# from database.database_1 import SessionLocal
# from database import tables
#
# with SessionLocal() as session:
#     users = session.query(tables.Users).filter(
#         tables.Users.id.between(10, 50),
#         tables.Users.age.between(20, 30)
#     ).order_by(
#         tables.Users.id.desc()
#     ).all()
#
#     for user in users:
#         print({
#             column.name: getattr(user, column.name)
#             for column in user.__table__.columns
#         })

# from database.database_1 import SessionLocal
# from database import tables
#
#
# with SessionLocal() as session:
#     user = session.get(tables.Users)
#
#     if user is not None:
#         print({
#             column.name: getattr(user, column.name)
#             for column in user.__table__.columns
#         })
#     else:
#         print("Пользователь не найден")
#




# from database.database_1 import SessionLocal
# from database import tables
#
# with SessionLocal() as session:
#     users = session.query(tables.Users).limit(10).all()
#
#     for user in users:
#         print({
#             column.name: getattr(user, column.name)
#             for column in user.__table__.columns
#         })
#
#
#

# """
# Пример объекта на котором вы можете потренироваться, используя pydantic схемы.
#
# Example of object for training with pydantic schemas.
# """
#
# computer = {
#     "id": 21,
#     "status": "ACTIVE",
#     "activated_at": "2013-06-01",
#     "expiration_at": "2040-06-01",
#     "host_v4": "91.192.222.17",
#     "host_v6": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
#     "detailed_info": {
#         "physical": {
#             "color": 'green',
#             "photo": 'https://images.unsplash.com/photo-1587831990711-23ca6441447b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8ZGVza3RvcCUyMGNvbXB1dGVyfGVufDB8fDB8fA%3D%3D&w=1000&q=80',
#             "uuid": "73860f46-5606-4912-95d3-4abaa6e1fd2c"
#         },
#         "owners": [{
#             "name": "Stephan Nollan",
#             "card_number": "4000000000000002",
#             "email": "shtephan.nollan@gmail.com",
#         }]
#     }
# }
#
#
#
#
#
#
#
# id
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