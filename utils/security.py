import bcrypt
from sqlalchemy.orm import Session
from models.user import (
  User
)
from email_validator import (
  validate_email,
  EmailNotValidError
)
from crud.user import (
  get_user_by
)
from config.settings import settings
from jose import (
  jwt,
  JWTError
)
import datetime
from fastapi import Depends
from utils.user_types import Role
from schema.user import (
  UserResponse
)
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer, OAuth2
from database.db_config import get_db
from sqlalchemy import Column
from typing import Tuple, Optional, Any
import httpx

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def hash_password(password:str)->str:
  password = password.encode("utf-8")
  salt = bcrypt.gensalt()
  hashed_password = bcrypt.hashpw(password=password, salt=salt)
  return hashed_password

def verify_password(password:str)->bool:
  return bcrypt.checkpw(password.encode("utf-8"), hash_password(password))

def authenticate_user(db: Session, username_or_email:str, 
                      password: str) -> Optional[Tuple[User, Any]]:
  try:
    validate_email(username_or_email)
    query_filter = User.email
  except EmailNotValidError:
    query_filter = User.username

  user = get_user_by(query_filter, db, username_or_email)
  if not user or not verify_password(password):
    return
  
  return user, query_filter

def create_access_token(data: dict)-> str:
  to_encode = data.copy()
  expire = datetime.datetime.now(datetime.UTC) + datetime.timedelta(
    minutes=settings.ACCESS_TOKEN_MINUTES
  )
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, key= settings.SECRET_KEY, algorithm=settings.ALGORITHM)

  return encoded_jwt

def verify_token(token: str, db:Session)-> Optional[User]:
  try:
    payload = jwt.decode(token=token, key=settings.SECRET_KEY, algorithms=settings.ALGORITHM)
    username_or_email = payload.get("sub")
  except JWTError:
    return
  
  if not username_or_email:
    return
  
  try:
    validate_email(username_or_email)
    query_filter = User.email
  except EmailNotValidError:
    query_filter = User.username

  user = get_user_by(query_filter, db, username_or_email)
  return user

def get_current_user(token=Depends(oauth2_scheme), db: Session= Depends(get_db)):
  user = verify_token(token, db)

  if user:
    return user
  else:
    return None

def get_premium_user(user: User = Depends(get_current_user)):
  if user and user.role == Role.premium:
    return user
  else:
    return None

# def resolve_github_token(
#     access_token: str= Depends(OAuth2),
#     db: Session = Depends(get_db)
# )-> User:
#   user_response = httpx.get("https://api/github.com/user",
#                             headers={"Authorization": access_token}).json()
  
#   username = user_response.get("login", " ")
#   user = get_user_by(User.username, db, username)
#   if not user:
#     email = user_response.get("email", " ")
#     user  = get_user_by(User.email, db, email)
  
#   if not 