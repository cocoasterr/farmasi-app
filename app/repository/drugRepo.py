from sqlalchemy.orm import Session
from models.drugs import Drugs

def create(db: Session, payload, model):
    new_data = model(**payload)
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

def read(db: Session, obat_id, model):
    return db.query(model).filter(model.id == obat_id).first()

def index(model, db: Session, skip: int = 0, limit: int = 100):
    return db.query(model).offset(skip).limit(limit).all()

def update(db: Session, obat_id, obat_data):
    obat = read(db, obat_id)
    if obat:
        for key, value in obat_data.items():
            setattr(obat, key, value)
        db.commit()
        db.refresh(obat)
        return obat

def delete(db: Session, obat_id):
    obat = read(db, obat_id)
    if obat:
        db.delete(obat)
        db.commit()
