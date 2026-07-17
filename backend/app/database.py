from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session

from typing import Generator

from app.config import DATABASE_URL

# CREATING THE CONNECTION ENGINE
engine = create_engine(DATABASE_URL)

# CREATING A FACTORY FOR DATABASE SESSIONS
SessionLocal = sessionmaker(
    bind = engine,
    autoflush = False,
    autocommit = False,
)

# BASE CASE FOR ALL DATABASE MODELS
class Base(DeclarativeBase):
    pass

def get_db_session() -> Generator[Session, None, None]:

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close() 