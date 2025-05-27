# from fastapi import APIRouter, Depends
# from database.db_config import get_db
# from sqlalchemy.orm import Session
# from models.items import Item

# router = APIRouter()

# @router.get("/items")
# async def get_items(db:Session=Depends(get_db)):
#   return db.query(Item).all()

# @router.post("/item")
# async def create_item(db:Session=Depends(get_db)):
#   new_item = Item(title="item title", description="item desc")
#   db.add(new_item)
#   db.commit()
#   db.refresh(new_item)
#   return new_item