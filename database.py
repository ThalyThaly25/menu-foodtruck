from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv("postgresql://uncle2302:GO6uBqN2TyT7tFYtTLIEfqu7cdZjyq4G@dpg-d70a74hr0fns73cnkolg-a/unclemoro_db")

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}  # necesario para SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

