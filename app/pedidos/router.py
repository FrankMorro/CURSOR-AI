from fastapi import APIRouter

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@router.get("/")
def listar_pedidos():
    """Lista todos los pedidos (ejemplo básico)."""
    return {"message": "Lista de pedidos - Implementar CRUD completo"} 