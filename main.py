from typing import List

from fastapi import APIRouter, FastAPI, HTTPException, status

from schemas import Plato
from settings import settings

app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.version,
    debug=settings.debug
)

# Base de datos en memoria
platos_db: List[Plato] = [
    Plato(id=1, nombre="Arepa", precio=50.00),
    Plato(id=2, nombre="Pabellón Criollo", precio=180.00),
    Plato(id=3, nombre="Cachapa", precio=90.00),
    Plato(id=4, nombre="Hallaca", precio=120.00),
    Plato(id=5, nombre="Tequeños", precio=60.00)
]

router = APIRouter(prefix="/platos", tags=["Platos"])

@router.get("/", response_model=List[Plato], summary="Listar todos los platos")
def listar_platos():
    """Devuelve la lista de todos los platos disponibles."""
    return platos_db

@router.get("/{plato_id}", response_model=Plato, summary="Obtener un plato por ID")
def obtener_plato(plato_id: int):
    """Devuelve un plato específico por su ID."""
    for plato in platos_db:
        if plato.id == plato_id:
            return plato
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plato no encontrado")

@router.post("/", response_model=Plato, status_code=status.HTTP_201_CREATED, summary="Crear un nuevo plato")
def crear_plato(plato: Plato):
    """Crea un nuevo plato. El ID debe ser único."""
    if any(p.id == plato.id for p in platos_db):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El ID ya existe")
    platos_db.append(plato)
    return plato

@router.put("/{plato_id}", response_model=Plato, summary="Actualizar un plato existente")
def actualizar_plato(plato_id: int, plato: Plato):
    """Actualiza los datos de un plato existente por su ID. El ID no puede ser modificado."""
    if plato_id != plato.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El ID del plato en la ruta y en el cuerpo deben ser iguales. El identificador no puede ser modificado."
        )
    for idx, p in enumerate(platos_db):
        if p.id == plato_id:
            platos_db[idx] = plato
            return plato
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plato no encontrado")

@router.delete("/{plato_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Eliminar un plato por ID")
def eliminar_plato(plato_id: int):
    """Elimina un plato específico por su ID."""
    for idx, p in enumerate(platos_db):
        if p.id == plato_id:
            platos_db.pop(idx)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plato no encontrado")

# @router.delete("/", status_code=status.HTTP_204_NO_CONTENT, summary="Eliminar todos los platos")
# def limpiar_platos():
#     """Elimina todos los platos de la lista."""
#     platos_db.clear()
#     return

app.include_router(router)

@app.get("/", summary="Mensaje de bienvenida")
def read_root():
    """Mensaje de bienvenida para la API."""
    return {"message": "¡Hola, FastAPI!"} 