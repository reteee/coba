import os
from sqlalchemy import Column, Integer, String, Boolean, UnicodeText
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from pelerbot import DATABASE_URL, MONGO_DB
import motor.motor_asyncio

mongo_db = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB)
db = mongo_db["SPAMBOT"]
SPAMBOT = 'SPAMBOT'
def start() -> scoped_session:
    engine = create_engine(DATABASE_URL)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

def start() -> scoped_session:
    dbi_url = DATABASE_URL
    engine = create_engine(DATABASE_URL)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

try:
    BASE = declarative_base()
    SESSION = start()
except AttributeError as e:
    print(
        "DB_URI is not configured. Features depending on the database might have issues."
    )
    print(str(e))


DB_AVAILABLE = False
BOTINLINE_AVAIABLE = False

def mulaisql() -> scoped_session:
    global DB_AVAILABLE
    engine = create_engine(DATABASE_URL, client_encoding="utf8")
    BASE.metadata.bind = engine
    try:
        BASE.metadata.create_all(engine)
    except exc.OperationalError:
        DB_AVAILABLE = False
        return False
    DB_AVAILABLE = True
    return scoped_session(sessionmaker(bind=engine, autoflush=False))
