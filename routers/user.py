from fastapi import APIRouter, Depends, HTTPException, status
from schema.user import User, CreateUser, UserResponse
from database.db_config import get_db
from sqlalchemy.orm import Session
from crud.user import (
  add_user,
  get_users,
)
from exceptions.exceptions import ResourceExistsError
from typing import List
from utils.user_types import Role

router = APIRouter()

@router.post("/user", response_model=UserResponse)
async def create_user(user: CreateUser, role: Role= Role.basic, db:Session = Depends(get_db)):
  new_user = add_user(role=role, db=db, user=user)

  if not new_user:
    raise ResourceExistsError(message="user already exits")

  return UserResponse.model_validate(new_user).model_dump(exclude_none=True)

@router.get("/users", response_model=List[UserResponse])
async def get_user(db:Session=Depends(get_db)):
  users = get_users(db)

  # users_response = [UserResponse.model_validate(user) for user in users]

  return [UserResponse.model_validate(user) for user in users]

