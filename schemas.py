from pydantic import BaseModel, Field

"""
Modelo de datos para el plato:

    Atributos:
        - id: Identificador único del plato
        - nombre: Nombre del plato
        - precio: Precio del plato

"""
class Plato(BaseModel):
    id: int = Field(..., title="ID del plato", description="Identificador único del plato")
    nombre: str = Field(..., title="Nombre del plato", max_length=100)
    precio: float = Field(..., title="Precio del plato", gt=0)

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "nombre": "Tacos al pastor",
                "precio": 120.50
            }
        } 