from sqlalchemy.orm import Session

from app.platos.crud import create_plato, get_platos
from app.platos.schemas import PlatoCreate
from database import get_db


# Crear algunos platos de ejemplo si la tabla está vacía
def poblar_platos(db: Session):
    if not get_platos(db, 0, 1):
        print("Agregando platos de ejemplo...")
        for i in range(1, 16):
            create_plato(db, PlatoCreate(nombre=f"Plato {i}", precio=10.0 + i))

# Probar la paginación
def probar_paginacion():
    db = next(get_db())
    poblar_platos(db)
    print("\nResultados de paginación (limit=5):")
    for page in range(0, 4):
        skip = page * 5
        platos = get_platos(db, skip=skip, limit=5)
        print(f"\nPágina {page + 1} (skip={skip}):")
        for plato in platos:
            print(f"  id={plato.id}, nombre={plato.nombre}, precio={plato.precio}")

if __name__ == "__main__":
    probar_paginacion()
