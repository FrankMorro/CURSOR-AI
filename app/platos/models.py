from sqlalchemy import Column, Integer, String, Float
from database import Base

class Plato(Base):
    __tablename__ = "platos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String, index=True)
    precio = Column(Float) 