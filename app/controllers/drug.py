from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from models.drugs import Drugs
from schemas.drugSchemas import DrugBaseSchema, DrugUpdateSchema
from database import get_db
from repository.drugRepo import create, index, read, update, delete

router = APIRouter()
app = FastAPI()

@app.post("/create")
def create_drug(payload: DrugBaseSchema, db: Session = Depends(get_db)):
    return create(db, payload)

@app.get("/{drug_id}")
def read_drug(drug_id: int, db: Session = Depends(get_db)):
    obat = read(db, drug_id)
    if obat is None:
        raise HTTPException(status_code=404, detail="Obat not found")
    return obat

@app.get("/")
def read_drug(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    obats = index(db, skip, limit)
    return obats

@app.put("/{drug_id}")
def update_drug(drug_id: int, payload: DrugUpdateSchema, db: Session = Depends(get_db)):
    obat = update(db, drug_id, payload)
    if obat is None:
        raise HTTPException(status_code=404, detail="Obat not found")
    return obat

@app.delete("/{drug_id}")
def delete_drug(drug_id: int, db: Session = Depends(get_db)):
    obat = read(db, drug_id)
    if obat is None:
        raise HTTPException(status_code=404, detail="Obat not found")
    delete(db, drug_id)
    return obat






