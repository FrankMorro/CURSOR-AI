from app.platos.crud import create_plato
from app.platos.schemas import PlatoCreate
from database import get_db

platos_ejemplo = [
    {"nombre": "Arepa Reina Pepiada", "precio": 60.0},
    {"nombre": "Pabellón Criollo", "precio": 180.0},
    {"nombre": "Cachapa con Queso", "precio": 90.0},
    {"nombre": "Hallaca", "precio": 120.0},
    {"nombre": "Empanada de Queso", "precio": 40.0},
    {"nombre": "Empanada de Carne", "precio": 45.0},
    {"nombre": "Tequeños", "precio": 70.0},
    {"nombre": "Perico Venezolano", "precio": 55.0},
    {"nombre": "Asado Negro", "precio": 200.0},
    {"nombre": "Polvorosa de Pollo", "precio": 110.0},
    {"nombre": "Tostones", "precio": 35.0},
    {"nombre": "Quesillo", "precio": 50.0},
    {"nombre": "Tres Leches", "precio": 60.0},
    {"nombre": "Chicha Venezolana", "precio": 30.0},
    {"nombre": "Mandoca", "precio": 25.0},
    {"nombre": "Pastel de Chucho", "precio": 150.0},
    {"nombre": "Cazón en Coco", "precio": 130.0},
    {"nombre": "Sancocho", "precio": 100.0},
    {"nombre": "Pisca Andina", "precio": 80.0},
    {"nombre": "Cachito de Jamón", "precio": 35.0},
]

def cargar_platos():
    db = next(get_db())
    for plato in platos_ejemplo:
        create_plato(db, PlatoCreate(**plato))
    print("✅ Platos de ejemplo cargados correctamente.")

if __name__ == "__main__":
    cargar_platos()
