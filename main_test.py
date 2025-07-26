from fastapi import FastAPI

from settings import settings

app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.version,
    debug=settings.debug
)

@app.get("/")
def read_root():
    return {"message": "¡Hola, FastAPI con configuración completa!"}

@app.get("/test-db")
def test_db():
    try:
        from sqlalchemy import text

        from database import engine
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            return {"message": "Conexión a DB exitosa", "result": result.fetchone()[0]}
    except Exception as e:
        import traceback
        return {
            "error": str(e),
            "error_type": type(e).__name__,
            "traceback": traceback.format_exc()
        }

@app.get("/test-url")
def test_url():
    try:
        from settings import settings

        # Mostrar la URL sin la contraseña por seguridad
        url_parts = settings.get_db_url().split('@')
        safe_url = f"{url_parts[0].split(':')[0]}:***@{url_parts[1]}"
        return {
            "db_host": settings.db_host,
            "db_port": settings.db_port,
            "db_name": settings.db_name,
            "db_user": settings.db_user,
            "safe_url": safe_url
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/config")
def show_config():
    try:
        from settings import settings
        return {
            "db_host": settings.db_host,
            "db_port": settings.db_port,
            "db_name": settings.db_name,
            "db_user": settings.db_user,
            "db_password_length": len(settings.db_password) if settings.db_password else 0,
            "db_password_set": bool(settings.db_password),
            "env_file_used": ".env" if settings.db_password else "No se detectó archivo .env"
        }
    except Exception as e:
        return {"error": str(e)} 