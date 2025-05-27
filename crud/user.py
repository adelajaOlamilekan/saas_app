from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy import Column
from schema.user import (
  CreateUser,
)
from models.user import User
from utils.user_types import Role
# from utils.security import hash_password

def add_user(db:Session,
             user:CreateUser,
             role: Role
             )-> User | None:
  # hashed_password = hash_password(user.password)
  new_user = User(**user.model_dump(exclude=["password"]), hashed_password=user.password, role=role)

  db.add(new_user)
  
  try:
    db.commit()
    db.refresh(new_user)
  except IntegrityError:
    db.rollback()
    return
  
  return new_user

def get_users(db:Session):
  users = db.query(User).order_by(User.created_at.desc()).all()

  return users

def get_user_by(query_filter: Column[str], db:Session, username_or_email: str):
  user = db.query(User).filter(query_filter == username_or_email).first()

  return user
