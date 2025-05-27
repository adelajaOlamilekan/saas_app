from database.db_config import Base
from sqlalchemy import (
  Integer,
  Column,
  String,
  DateTime,
  func,
  Enum
)
from utils.user_types import Role

class User(Base):
  __tablename__="users"
  id = Column(Integer, primary_key=True)
  username = Column(String)
  email = Column(String, unique=True)
  hashed_password = Column(String)
  role = Column(Enum(Role), default=Role.basic)
  created_at = Column(DateTime(timezone=True), default=func.now())
  updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

# Base.metadata.create_all(bind=engine)