from sqlalchemy import Column, Float, Integer, String

from app.clientes.models import Cliente
# Importar todos los modelos de los diferentes dominios
from app.platos.models import Plato
from database import Base

# Exportar todos los modelos para que SQLAlchemy los reconozca
__all__ = ["Plato", "Cliente"] 
