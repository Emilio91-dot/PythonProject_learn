from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



model = declarative_base(name='Model')

DATABASE_URL = (
    "postgresql+psycopg2://postgres:1234@localhost:5432/emilgabdrahmanov"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)