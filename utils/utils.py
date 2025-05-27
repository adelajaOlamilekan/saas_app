import bcrypt

def hash_password(password:str)->str:
  password = password.encode("utf-8")
  salt = bcrypt.gensalt()
  hashed_password = bcrypt.hashpw(password=password, salt=salt)
  return hashed_password

def verify_password(password:str)->bool:
  return bcrypt.checkpw(password.encode("utf-8"), hash_password(password))