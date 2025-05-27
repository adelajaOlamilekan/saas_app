from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from schema.user import (
  CreateUser,
)
from models.user import User
from utils.utils import hash_password

def add_user(db:Session,
             user:CreateUser
             )-> User | None:
  hashed_password = hash_password(user.password)
  new_user = User(**user.model_dump(exclude=["password"]), hashed_password=hashed_password)

  db.add(new_user)
  
  try:
    db.commit()
    db.refresh(new_user)
  except IntegrityError:
    db.rollback()
    return
  
  return new_user