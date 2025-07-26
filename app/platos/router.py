from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db

from . import crud
from .schemas import Plato, PlatoCreate

router = APIRouter(prefix="/platos", tags=["Platos"])

@router.get("/", response_model=List[Plato], summary="Listar todos los platos")
def listar_platos(db: Session = Depends(get_db)):
    """Devuelve la lista de todos los platos disponibles."""
    return crud.get_platos(db)

@router.get("/{plato_id}", response_model=Plato, summary="Obtener un plato por ID")
def obtener_plato(plato_id: int, db: Session = Depends(get_db)):
    """Devuelve un plato específico por su ID."""
    db_plato = crud.get_plato(db, plato_id=plato_id)
    if db_plato is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plato no encontrado")
    return db_plato

@router.post("/", response_model=Plato, status_code=status.HTTP_201_CREATED, summary="Crear un nuevo plato")
def crear_plato(plato: PlatoCreate, db: Session = Depends(get_db)):
    """Crea un nuevo plato. El ID se genera automáticamente."""
    return crud.create_plato(db=db, plato=plato)

@router.put("/{plato_id}", response_model=Plato, summary="Actualizar un plato existente")
def actualizar_plato(plato_id: int, plato: Plato, db: Session = Depends(get_db)):
    """Actualiza los datos de un plato existente por su ID."""
    if plato_id != plato.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El ID del plato en la ruta y en el cuerpo deben ser iguales."
        )
    plato_data = {"nombre": plato.nombre, "precio": plato.precio}
    db_plato = crud.update_plato(db=db, plato_id=plato_id, plato_data=plato_data)
    if db_plato is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plato no encontrado")
    return db_plato

@router.delete("/{plato_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Eliminar un plato por ID")
def eliminar_plato(plato_id: int, db: Session = Depends(get_db)):
    """Elimina un plato específico por su ID."""
    db_plato = crud.delete_plato(db=db, plato_id=plato_id)
    if db_plato is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plato no encontrado")
    return

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT, summary="Eliminar todos los platos")
def limpiar_platos(db: Session = Depends(get_db)):
    """Elimina todos los platos de la base de datos."""
    crud.delete_all_platos(db=db)
    return 