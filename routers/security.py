from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database.db_config import get_db
from schema.token import Token
from utils.security import(
  authenticate_user,
  create_access_token,
  verify_token,
  get_premium_user,
  oauth2_scheme,
  get_current_user,

)
from models.user import User
from schema.user import UserResponse

router = APIRouter()

@router.post("/login", response_model=Token)
async def create_user_token(
  form_data:OAuth2PasswordRequestForm = Depends(),
  db:Session = Depends(get_db)
  ):
  user, query_filter = authenticate_user(db, form_data.username, form_data.password)

  if not user:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Incorrect username or password"
    )
  
  if query_filter == User.username:
    access_token = create_access_token(data={"sub": user.username})
  elif query_filter == User.email:
    access_token = create_access_token(data={"sub": user.email})
  
  return Token(access_token=access_token, token_type="bearer")

@router.get("/users/me")
def read_user_me(token:str = Depends(oauth2_scheme), db: Session =Depends(get_db)):
  user = verify_token(token=token, db=db)

  if not user:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="User not authorized"
    )
  
  return user

@router.get("/welcome/premium_user")
def welcome_premium_user(user: User = Depends(get_premium_user)):
  if user:
    return{
      "message": f"{user.username} welcome to the premium space"\
      f" you are a {user.role} user"
    }
  else:
    return HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="User not authorized"
    )

@router.get("/welcome/all_user")
def welcome_all_user(user: User = Depends(get_current_user)):
  if user:
    return {
      "message": f"Welcome to the basic space {user.username} you are a " \
      f"{user.role} user"
    }
  else:
    return HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="User not authorized"
    )