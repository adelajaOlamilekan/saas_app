from pydantic import BaseModel, EmailStr, ConfigDict
from enum import Enum
from utils.user_types import Role
from datetime import datetime

class User(BaseModel):
  username: str
  email: EmailStr

class CreateUser(User):
  password: str

class ResponseBase(BaseModel):
  created_at: datetime
  updated_at: datetime

class UserResponse(ResponseBase, User):
  role: Role
  model_config = ConfigDict(from_attributes=True)