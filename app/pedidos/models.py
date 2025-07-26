from sqlalchemy import Column, Float, Integer, String

from database import Base


class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_cliente = Column(Integer, index=True)
    fecha = Column(String, unique=False, index=True)
    monto = Column(Float, default=0) 