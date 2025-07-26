from sqlalchemy import Column, Float, ForeignKey, Integer, String

from base import Base


class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_cliente = Column(Integer, ForeignKey("clientes.id", ondelete="RESTRICT"), index=True)
    fecha = Column(String, unique=False, index=True)
    monto = Column(Float, default=0)