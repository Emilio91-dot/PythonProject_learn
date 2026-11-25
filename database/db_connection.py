from sqlalchemy import text

from database.database import engine


def main() -> None:
    """Print a small sample from the users table."""
    with engine.connect() as connection:
        rows = connection.execute(text("SELECT * FROM users LIMIT 10"))
        for row in rows:
            print(row)


if __name__ == "__main__":
    main()
