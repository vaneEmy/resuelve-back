from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base

DB_URL = "sqlite:///resuelve.db"

Base = declarative_base()