from typing import Optional

from pydantic import BaseModel, Field


class PlatoCreate(BaseModel):
    nombre: str = Field(..., title="Nombre del plato", max_length=100)
    precio: float = Field(..., title="Precio del plato", gt=0)

    class Config:
        json_schema_extra = {
            "example": {
                "nombre": "Arepa",
                "precio": 50.0
            }
        }

class Plato(BaseModel):
    id: Optional[int] = Field(None, title="ID del plato", description="Identificador único del plato (se genera automáticamente)")
    nombre: str = Field(..., title="Nombre del plato", max_length=100)
    precio: float = Field(..., title="Precio del plato", gt=0)

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "nombre": "Arepa",
                "precio": 50.0
            }
        } 