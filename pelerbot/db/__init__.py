from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from pelerbot import DATABASE_URL

if DATABASE_URL.startswith("postgres://"):
    uri = DATABASE_URL.replace("postgres://", "postgresql://", 1)
else:
    uri = DATABASE_URL


def start() -> scoped_session:
    engine = create_engine(DATABASE_URL)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

try:
    BASE = declarative_base()
    SESSION = start()
except AttributeError as e:
    print(
        "DB_URI tidak dikonfigurasi. Fitur yang membutuhkan database mengalami masalah."
    )
    print(str(e))
