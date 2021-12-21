from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from common.config import db_config


DB_URL = db_config.DATABASE_URL + '?charset=utf8'
engine = create_engine(DB_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
BaseModel = declarative_base()


def init_database():
    BaseModel.metadata.create_all(engine)


def get_session():
    session = session_local()
    try:
        yield session
    finally:
        session.close()
