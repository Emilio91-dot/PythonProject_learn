# from sqlalchemy import create_engine, text
#
# engine = create_engine(
#     "postgresql+psycopg2://postgres:1234@localhost:5432/emilgabdrahmanov"
# )
#
# with engine.connect() as conn:
#     db_name = conn.execute(
#         text("SELECT current_database();")
#     ).scalar()
#
#     print(f"Подключен к БД: {db_name}")


from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://postgres:1234@localhost:5432/emilgabdrahmanov"
)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM users LIMIT 10"))

    for row in result:
        print(row)