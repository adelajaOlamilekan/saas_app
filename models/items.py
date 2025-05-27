from database.db_config import Base
from sqlalchemy import (
  Integer,
  Column,
  String,
  DateTime,
  func,
)


class Item(Base):
  __tablename__="items"
  id = Column(Integer, primary_key=True)
  title = Column(String)
  description = Column(String)
  created_at = Column(DateTime(timezone=True), default=func.now())
  updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
