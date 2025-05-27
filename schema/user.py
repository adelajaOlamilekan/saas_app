from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime

class User(BaseModel):
  username: str
  email: EmailStr

class CreateUser(User):
  password: str

class ResponseBase(BaseModel):
  created_at: datetime
  updated_at: datetime
  message: str | None = None

class UserResponse(ResponseBase, User):
  model_config = ConfigDict(from_attributes=True)