from fastapi import APIRouter

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("/")
def listar_clientes():
    """Lista todos los clientes (ejemplo básico)."""
    return {"message": "Lista de clientes - Implementar CRUD completo"} 