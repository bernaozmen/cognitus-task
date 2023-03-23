from sqlalchemy import create_engine, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import find_dotenv, load_dotenv
import redis
from config import settings

load_dotenv(find_dotenv())

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()