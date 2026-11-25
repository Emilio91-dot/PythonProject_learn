"""Пример запроса к таблице пользователей и вывода найденных записей."""

from database import tables
from database.database_1 import SessionLocal


def main():
    """Показать пользователей с ID от 10 до 50 и возрастом от 20 до 30."""
    with SessionLocal() as session:
        users = (
            session.query(tables.Users)
            .filter(
                tables.Users.id.between(10, 50),
                tables.Users.age.between(20, 30),
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
