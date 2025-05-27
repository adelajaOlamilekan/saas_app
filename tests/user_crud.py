# def add_user(session:Session,
#              user:CreateUser
#              )-> User | None:

from sqlalchemy.orm import Session
from crud.user import (
  add_user
)
from schema.user import(
  CreateUser,
)

def test_add_user_successfully(session: Session, new_user: CreateUser):
  created_user = add_user(session, new_user)

  assert created_user is not None

def test_add_duplicate_user(session: Session, new_user: CreateUser):
  created_user = add_user(session, new_user)
  created_user = add_user(session, new_user)

  assert created_user is None