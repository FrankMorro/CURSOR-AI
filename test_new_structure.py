#!/usr/bin/env python3
"""
Script de prueba para verificar que la nueva estructura funciona correctamente.
"""

def test_imports():
    """Prueba que todas las importaciones funcionen correctamente."""
    try:
        # Probar importación de la aplicación principal
        from app.main import app
        print("✅ Importación de app.main exitosa")
        
        # Probar importación de modelos
        from app.clientes.models import Cliente
        from app.platos.models import Plato
        print("✅ Importación de modelos exitosa")
        
        # Probar importación de esquemas
        from app.platos.schemas import Plato, PlatoCreate
        print("✅ Importación de esquemas exitosa")
        
        # Probar importación de CRUD
        from app.platos import crud
        print("✅ Importación de CRUD exitosa")
        
        # Probar importación de routers
        from app.clientes.router import router as clientes_router
        from app.pedidos.router import router as pedidos_router
        from app.platos.router import router as platos_router
        print("✅ Importación de routers exitosa")
        
        # Probar importación de configuración
        from database import get_db
        from settings import settings
        print("✅ Importación de configuración exitosa")
        
        print("\n🎉 ¡Todas las importaciones funcionan correctamente!")
        print("📝 Para ejecutar la API usa: uvicorn app.main:app --reload")
        
    except ImportError as e:
        print(f"❌ Error de importación: {e}")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print("🧪 Probando nueva estructura del proyecto...\n")
    test_imports() 