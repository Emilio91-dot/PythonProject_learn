from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Model = declarative_base()




# докер
DATABASE_URL = (
    "postgresql+psycopg2://postgres:1234@host.docker.internal:5432/emilgabdrahmanov"
)


# локально
# DATABASE_URL = (
#     "postgresql+psycopg2://postgres:1234@localhost:5432/emilgabdrahmanov"
# )

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# session = SessionLocal()