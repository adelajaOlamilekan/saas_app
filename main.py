from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from database.db_config import get_db, engine, Base
from sqlalchemy.orm import Session
from exceptions.exceptions import (
  ResourceExistsError
)
import routers
import routers.item
import routers.user
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app:FastAPI):
  Base.metadata.create_all(bind=engine)
  yield
  print("Thank you for banking with us")

app = FastAPI(
  title="SAAS APP",
  description="This is the API for a SAAS Application",
  version="1.0.0",
  lifespan=lifespan
)

app.include_router(routers.user.router)
# app.include_router(routers.item.router)

@app.get("/")
def home(db:Session = Depends(get_db)):
  return {"message": "Home page of the API"}

@app.exception_handler(ResourceExistsError)
async def user_not_created(request, exc:ResourceExistsError):
  return JSONResponse(
    status_code=exc.error_code,
    content={
      "message": exc.message
    }
  )