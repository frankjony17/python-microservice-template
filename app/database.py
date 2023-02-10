import sqlalchemy
from loguru import logger
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import CreateSchema
from sqlalchemy_utils import create_database, database_exists, drop_database

from app.internal.config import DATABASE_SCHEMA, DATABASE_URL, TESTING

if TESTING:
    if database_exists(DATABASE_URL):
        drop_database(DATABASE_URL)

    create_database(DATABASE_URL)


# Postgres Database Configuration
try:
    engine = sqlalchemy.create_engine(DATABASE_URL, pool_pre_ping=True)

    if not engine.dialect.has_schema(engine, DATABASE_SCHEMA):
        engine.execute(CreateSchema(DATABASE_SCHEMA))

    logger.success("[+] Create database engine")
except SQLAlchemyError as error:
    logger.opt(exception=True).error(f"[-] Error connecting to {DATABASE_URL}: {error}")
    raise


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
