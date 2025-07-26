from sqlalchemy import Boolean, Column, Integer, String

from database import Base


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    activo = Column(Boolean, default=True) 