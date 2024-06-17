from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Annotated
from database import engine, SessionLocal
from pydantic import BaseModel
from models.Item import Item, Base  # Importez directement Item et Base

app = FastAPI()

# Créez toutes les tables de base de données
Base.metadata.create_all(bind=engine)

# Schéma
class ItemSchema(BaseModel):
    name: str
    description: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemSchema, db: db_dependency):
    db_item = Item(**item.dict())  # Utilisez item.dict() pour convertir le schéma en dictionnaire
    db.add(db_item)
    db.commit()
    db.refresh(db_item)  # Ajoutez cette ligne pour rafraîchir l'élément créé
    return {"message": "Item created successfully", "item": db_item}

@app.get("/items/")
async def read_items(db: db_dependency):
    db_items = db.query(Item).all()  # Assurez-vous que Item est correctement importé
    return [{"id": item.id, "name": item.name, "description": item.description} for item in db_items]

@app.get("/items/{item_id}")
async def read_item(item_id: int, db: db_dependency):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return {"id": db_item.id, "item": db_item.name}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: ItemSchema, db: db_dependency):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    db_item.name = item.name
    db_item.description = item.description  # Assurez-vous de mettre à jour la description aussi
    db.commit()
    db.refresh(db_item)  # Rafraîchir l'élément mis à jour
    return {"message": "Item updated successfully", "item": db_item}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int, db: db_dependency):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted successfully"}
