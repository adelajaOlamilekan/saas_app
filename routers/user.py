from fastapi import APIRouter, Depends, HTTPException, status
from schema.user import User, CreateUser, UserResponse
from database.db_config import get_db
from sqlalchemy.orm import Session
from crud.user import add_user
from exceptions.exceptions import ResourceExistsError

router = APIRouter()

@router.post("/user", response_model=UserResponse)
async def create_user(user: CreateUser, db:Session = Depends(get_db)):
  new_user = add_user(db=db, user=user)

  if not new_user:
    raise ResourceExistsError(message="user already exits")

  return UserResponse.model_validate(new_user).model_dump(exclude_none=True)

