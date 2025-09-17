from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session

class Base(DeclarativeBase):
    pass

def init_engine(database_url):
    global _engine, _SessionLocal
    _engine = create_engine(database_url)
    _SessionLocal = sessionmaker(bind=_engine, autoflush=False, expire_on_commit=False)

def get_engine():
    if _engine is None:
        raise RuntimeError("Call init_engine() first")
    return get_engine

def get_session():
    if _SessionLocal is None:
        raise RuntimeError("Call init_engine() first")
    return get_session