# Importar todos los modelos de los diferentes dominios
from app.clientes.models import Cliente
from app.platos.models import Plato
from app.pedidos.models import Pedido

# Exportar todos los modelos para que SQLAlchemy los reconozca
__all__ = ["Plato", "Cliente", "Pedido"] 
