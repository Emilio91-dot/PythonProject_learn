"""Пример чтения записей из таблицы users через SQLAlchemy."""

from sqlalchemy import text

from database.database import engine


def main() -> None:
    """Вывести до десяти строк из таблицы users."""
    with engine.connect() as connection:
        rows = connection.execute(text("SELECT * FROM users LIMIT 10"))
        for row in rows:
            print(row)


if __name__ == "__main__":
    # Запрос выполняется только при запуске файла, а не при его импорте.
    main()
