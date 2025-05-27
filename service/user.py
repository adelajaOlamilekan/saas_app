from sqlalchemy.orm import Session
from schema.user import(
  CreateUser
)
from utils.security import hash_password
from crud.user import (
  add_user,
)

def create_user(db:Session, user:CreateUser):
  user.password = hash_password(user.password)
  created_user = add_user(db, user)
  return created_user
