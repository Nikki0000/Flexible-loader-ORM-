from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

def get_engine(db_url):
    return create_engine(db_url)

def get_session(engine):
    return sessionmaker(bind=engine)