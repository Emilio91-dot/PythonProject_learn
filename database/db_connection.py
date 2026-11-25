"""Пример чтения записей пользователей из настроенной базы данных."""

from sqlalchemy import text

from database.database_1 import engine


def main() -> None:
    """Вывести до десяти строк из таблицы users."""
    with engine.connect() as connection:
        for row in connection.execute(text("SELECT * FROM users LIMIT 10")):
            print(row)


if __name__ == "__main__":
    # Запрос выполняется только при запуске файла, а не при его импорте.
    main()
