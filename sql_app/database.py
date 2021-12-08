from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# create database
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# If you were using a PostgreSQL database instead
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# create a SQLAlchemy "engine"
# connect_args={"check_same_thread": False - is needed only for SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


#Later we will inherit from this class to create each of the database models or classes 
Base = declarative_base()