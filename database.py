from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import models  # Importa todos los modelos para que se registren
from base import Base  # Importa la instancia única de Base
from settings import settings

# Crear el motor de base de datos con configuración de codificación
engine = create_engine(
    settings.get_db_url(),
    pool_pre_ping=True,
    connect_args={
        "client_encoding": "utf8"
    }
)

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear las tablas en la base de datos (incluyendo todos los modelos importados)
Base.metadata.create_all(bind=engine)
