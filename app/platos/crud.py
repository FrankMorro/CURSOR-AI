from sqlalchemy import text
from sqlalchemy.orm import Session

from .models import Plato
from .schemas import PlatoCreate


def get_platos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Plato).offset(skip).limit(limit).all()

def get_plato(db: Session, plato_id: int):
    return db.query(Plato).filter(Plato.id == plato_id).first()

def create_plato(db: Session, plato: PlatoCreate):
    db_plato = Plato(nombre=plato.nombre, precio=plato.precio)
    db.add(db_plato)
    db.commit()
    db.refresh(db_plato)
    return db_plato

def update_plato(db: Session, plato_id: int, plato_data: dict):
    db_plato = db.query(Plato).filter(Plato.id == plato_id).first()
    if db_plato:
        for key, value in plato_data.items():
            setattr(db_plato, key, value)
        db.commit()
        db.refresh(db_plato)
    return db_plato

def delete_plato(db: Session, plato_id: int):
    db_plato = db.query(Plato).filter(Plato.id == plato_id).first()
    if db_plato:
        db.delete(db_plato)
        db.commit()
    return db_plato

def delete_all_platos(db: Session):
    db.query(Plato).delete()
    db.commit() 