from sqlalchemy import Column, Float, Integer, String

from database import Base


class Plato(Base):
    __tablename__ = "platos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String, index=True)
    precio = Column(Float) 