from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.clientes.router import router as clientes_router
from app.pedidos.router import router as pedidos_router
# Importar routers de diferentes dominios
from app.platos.router import router as platos_router
from database import engine
from models import Base
from settings import settings


def create_tables():
    Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    create_tables()
    yield
    # Shutdown (opcional)

app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.version,
    debug=settings.debug,
    lifespan=lifespan
)

# Incluir routers de diferentes dominios
app.include_router(platos_router, prefix="/api/v1")
app.include_router(clientes_router, prefix="/api/v1")
app.include_router(pedidos_router, prefix="/api/v1")

@app.get("/", summary="Mensaje de bienvenida")
def read_root():
    """Mensaje de bienvenida para la API."""
    return {"message": "¡Hola, FastAPI!"} 