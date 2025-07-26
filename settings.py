from typing import List, Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Información general de la API
    app_name: str = "FastAPI Simple"
    app_description: str = "API de ejemplo creada con FastAPI"
    version: str = "0.1.0"
    debug: bool = True

    # Configuración del Servidor
    server_host: str = "0.0.0.0"
    server_port: int = 8000

    # Configuración de la Base de Datos
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "fastapi_simple"
    db_user: str = "postgres"
    db_password: str = ""  # Debe venir del archivo .env
    db_url: Optional[str] = None

    # Configuración de CORS
    allowed_hosts: List[str] = ["*"]
    allowed_methods: List[str] = ["*"]
    allowed_headers: List[str] = ["*"]

    # Documentación
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    openapi_url: str = "/openapi.json"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    def get_db_url(self):
        if self.db_url:
            return self.db_url
        # Usar quote_plus para manejar caracteres especiales en la contraseña
        from urllib.parse import quote_plus
        password = quote_plus(self.db_password)
        return f"postgresql://{self.db_user}:{password}@{self.db_host}:{self.db_port}/{self.db_name}"

settings = Settings() 