# Importar todos los modelos de los diferentes dominios
from sqlalchemy.orm import declarative_base

from app.clientes.models import Cliente
from app.pedidos.models import Pedido
from app.platos.models import Plato

Base = declarative_base()

# Exportar todos los modelos para que SQLAlchemy los reconozca
__all__ = ["Plato", "Cliente", "Pedido", "Base"]
