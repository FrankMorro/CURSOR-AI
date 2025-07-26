from typing import List

from fastapi import APIRouter, Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from crud import (create_plato, delete_all_platos, delete_plato, get_plato,
                  get_platos, update_plato)
from database import engine, get_db
from models import Base
from schemas import Plato, PlatoCreate
from settings import settings

app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.version,
    debug=settings.debug
)

# Crear las tablas en la base de datos
def create_tables():
    Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/platos", tags=["Platos"])

@router.get("/", response_model=List[Plato], summary="Listar todos los platos")
def listar_platos(db: Session = Depends(get_db)):
    """Devuelve la lista de todos los platos disponibles."""
    return get_platos(db)

@router.get("/{plato_id}", response_model=Plato, summary="Obtener un plato por ID")
def obtener_plato(plato_id: int, db: Session = Depends(get_db)):
    """Devuelve un plato específico por su ID."""
    db_plato = get_plato(db, plato_id=plato_id)
    if db_plato is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plato no encontrado")
    return db_plato

@router.post("/", response_model=Plato, status_code=status.HTTP_201_CREATED, summary="Crear un nuevo plato")
def crear_plato(plato: PlatoCreate, db: Session = Depends(get_db)):
    """Crea un nuevo plato. El ID se genera automáticamente."""
    return create_plato(db=db, plato=plato)

@router.put("/{plato_id}", response_model=Plato, summary="Actualizar un plato existente")
def actualizar_plato(plato_id: int, plato: Plato, db: Session = Depends(get_db)):
    """Actualiza los datos de un plato existente por su ID. El ID no puede ser modificado."""
    if plato_id != plato.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El ID del plato en la ruta y en el cuerpo deben ser iguales. El identificador no puede ser modificado."
        )
    db_plato = update_plato(db=db, plato_id=plato_id, plato=plato)
    if db_plato is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plato no encontrado")
    return db_plato

@router.delete("/{plato_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Eliminar un plato por ID")
def eliminar_plato(plato_id: int, db: Session = Depends(get_db)):
    """Elimina un plato específico por su ID."""
    db_plato = delete_plato(db=db, plato_id=plato_id)
    if db_plato is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plato no encontrado")
    return

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT, summary="Eliminar todos los platos")
def limpiar_platos(db: Session = Depends(get_db)):
    """Elimina todos los platos de la base de datos."""
    delete_all_platos(db=db)
    return

app.include_router(router)

@app.get("/", summary="Mensaje de bienvenida")
def read_root():
    """Mensaje de bienvenida para la API."""
    return {"message": "¡Hola, FastAPI!"}

# Crear las tablas al iniciar la aplicación
@app.on_event("startup")
async def startup_event():
    create_tables() 