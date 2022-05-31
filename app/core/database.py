from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import config

if config.DB_TYPE == 'sqlite':
    connect_args = {'check_same_thread': False}
else:
    connect_args = {}

engine = create_engine(
    config.DB_URL,
    connect_args=connect_args
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
