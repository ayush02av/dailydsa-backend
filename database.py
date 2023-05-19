from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import config

DATABASE_URL = f"{config.DB_HOSTTYPE}://{config.DB_USERNAME}:{config.DB_PASSWORD}@{config.DB_HOSTNAME}/{config.DB_DATABASE}" + '?ssl={"rejectUnauthorized":true}'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()