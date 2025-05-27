from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine

DB_URL = "sqlite:///./saas.db"

class Base(DeclarativeBase):
  pass


engine = create_engine(url=DB_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
  
# def get_engine():
#   yield engine