# API FastAPI con PostgreSQL - Guía Completa

## 📋 Tabla de Contenidos
1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Tecnologías Utilizadas](#tecnologías-utilizadas)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Conceptos Básicos](#conceptos-básicos)
5. [Configuración Inicial](#configuración-inicial)
6. [Explicación Detallada de Cada Archivo](#explicación-detallada-de-cada-archivo)
7. [Cómo Funciona la API](#cómo-funciona-la-api)
8. [Endpoints Disponibles](#endpoints-disponibles)
9. [Ejemplos de Uso](#ejemplos-de-uso)
10. [Flujo de Datos](#flujo-de-datos)
11. [Mejores Prácticas Implementadas](#mejores-prácticas-implementadas)
12. [Solución de Problemas](#solución-de-problemas)

---

## 🎯 Descripción del Proyecto

Esta es una API REST completa construida con **FastAPI** y **PostgreSQL** que implementa un sistema de gestión de platos de comida venezolana. La API incluye operaciones CRUD completas (Crear, Leer, Actualizar, Eliminar) con persistencia de datos en base de datos.

### ¿Qué hace esta API?
- ✅ Gestiona platos de comida venezolana
- ✅ Almacena datos en PostgreSQL
- ✅ Genera IDs automáticamente
- ✅ Valida datos de entrada
- ✅ Maneja errores apropiadamente
- ✅ Genera documentación automática

---

## 🛠 Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **Python** | 3.11+ | Lenguaje de programación |
| **FastAPI** | 0.116+ | Framework web moderno y rápido |
| **PostgreSQL** | 17.5+ | Base de datos relacional |
| **SQLAlchemy** | 2.0+ | ORM (Object-Relational Mapping) |
| **Pydantic** | 2.0+ | Validación de datos y serialización |
| **Uvicorn** | - | Servidor ASGI para FastAPI |
| **psycopg2** | - | Driver de PostgreSQL para Python |

---

## 📁 Estructura del Proyecto

```
proyecto/
│
├── 📄 main.py              # Punto de entrada de la aplicación
├── 📄 settings.py          # Configuración y variables de entorno
├── 📄 database.py          # Configuración de la base de datos
├── 📄 models.py            # Modelos SQLAlchemy (tablas)
├── 📄 schemas.py           # Esquemas Pydantic (validación)
├── 📄 crud.py              # Operaciones de base de datos
├── 📄 requirements.txt     # Dependencias del proyecto
├── 📄 .env                 # Variables de entorno (crear manualmente)
├── 📄 env_example.txt      # Plantilla de variables de entorno
└── 📄 README.md            # Esta documentación
```

---

## 🧠 Conceptos Básicos

### ¿Qué es FastAPI?
FastAPI es un framework web moderno para Python que permite crear APIs rápidas y fáciles de usar. Sus características principales son:

- **Rápido**: Rendimiento muy alto
- **Fácil de usar**: Sintaxis simple y intuitiva
- **Documentación automática**: Genera docs interactivas
- **Validación automática**: Valida datos de entrada y salida
- **Tipado estático**: Usa type hints de Python

### ¿Qué es PostgreSQL?
PostgreSQL es una base de datos relacional robusta y confiable que:
- Almacena datos de forma estructurada
- Permite consultas complejas
- Mantiene la integridad de los datos
- Es escalable y confiable

### ¿Qué es SQLAlchemy?
SQLAlchemy es un ORM (Object-Relational Mapping) que permite:
- Trabajar con bases de datos usando código Python
- No escribir SQL directamente
- Manejar conexiones de forma segura
- Migrar entre diferentes bases de datos

### ¿Qué es Pydantic?
Pydantic es una biblioteca para:
- Validar datos de entrada
- Serializar/deserializar datos
- Generar documentación automática
- Asegurar tipos de datos correctos

---

## ⚙️ Configuración Inicial

### 1. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 2. Configurar Base de Datos
```bash
# Crear la base de datos en PostgreSQL
createdb fastapi_simple
```

### 3. Crear Archivo .env
Crea un archivo `.env` en la raíz del proyecto:
```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=fastapi_simple
DB_USER=postgres
DB_PASSWORD=tu_contraseña_aqui
```

### 4. Ejecutar la API
```bash
uvicorn main:app --reload
```

---

## 📄 Explicación Detallada de Cada Archivo

### 🔧 settings.py - Configuración del Sistema

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Configuración de la API
    app_name: str = "FastAPI Simple"
    version: str = "0.1.0"
    
    # Configuración de la base de datos
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "fastapi_simple"
    db_user: str = "postgres"
    db_password: str = ""
    
    class Config:
        env_file = ".env"  # Lee variables del archivo .env
```

**¿Qué hace este archivo?**
- Define todas las configuraciones de la aplicación
- Lee variables de entorno del archivo `.env`
- Proporciona valores por defecto seguros
- Centraliza la configuración en un solo lugar

**¿Por qué es importante?**
- Evita hardcodear datos sensibles (contraseñas)
- Facilita cambiar configuraciones entre entornos
- Sigue el principio de "12-Factor App"

### 🗄️ database.py - Configuración de Base de Datos

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Crear el motor de base de datos
engine = create_engine(settings.get_db_url())

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

**¿Qué hace este archivo?**
- Configura la conexión a PostgreSQL
- Crea el motor de SQLAlchemy
- Maneja sesiones de base de datos
- Implementa el patrón de inyección de dependencias

**¿Por qué usar sesiones?**
- Cada request obtiene su propia conexión
- Las conexiones se cierran automáticamente
- Evita problemas de concurrencia
- Mejora el rendimiento

### 🏗️ models.py - Modelos de Base de Datos

```python
from sqlalchemy import Column, Integer, String, Float
from database import Base

class Plato(Base):
    __tablename__ = "platos"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String, index=True)
    precio = Column(Float)
```

**¿Qué hace este archivo?**
- Define la estructura de las tablas
- Mapea clases Python a tablas SQL
- Define tipos de datos y restricciones
- Configura índices para mejor rendimiento

**Conceptos importantes:**
- `primary_key=True`: Define la clave primaria
- `autoincrement=True`: ID se genera automáticamente
- `index=True`: Crea índices para búsquedas rápidas

### 📋 schemas.py - Validación de Datos

```python
from pydantic import BaseModel, Field

class PlatoCreate(BaseModel):
    nombre: str = Field(..., max_length=100)
    precio: float = Field(..., gt=0)

class Plato(BaseModel):
    id: Optional[int] = None
    nombre: str = Field(..., max_length=100)
    precio: float = Field(..., gt=0)
    
    class Config:
        from_attributes = True
```

**¿Qué hace este archivo?**
- Define la estructura de datos de entrada/salida
- Valida datos automáticamente
- Genera documentación automática
- Separa datos de creación de datos completos

**Diferencias importantes:**
- `PlatoCreate`: Solo para crear (sin ID)
- `Plato`: Para respuestas completas (con ID)
- `Field(...)`: Campo obligatorio
- `Field(..., gt=0)`: Validación (precio > 0)

### 🔄 crud.py - Operaciones de Base de Datos

```python
def create_plato(db: Session, plato: PlatoCreate):
    db_plato = Plato(nombre=plato.nombre, precio=plato.precio)
    db.add(db_plato)
    db.commit()
    db.refresh(db_plato)
    return db_plato

def get_platos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Plato).offset(skip).limit(limit).all()
```

**¿Qué hace este archivo?**
- Contiene todas las operaciones CRUD
- Separa lógica de negocio de lógica de API
- Maneja transacciones de base de datos
- Implementa paginación básica

**Operaciones CRUD:**
- **C**reate: `create_plato()`
- **R**ead: `get_platos()`, `get_plato()`
- **U**pdate: `update_plato()`
- **D**elete: `delete_plato()`, `delete_all_platos()`

### 🚀 main.py - Punto de Entrada

```python
from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy.orm import Session

app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.version
)

router = APIRouter(prefix="/platos", tags=["Platos"])

@router.post("/", response_model=Plato)
def crear_plato(plato: PlatoCreate, db: Session = Depends(get_db)):
    return create_plato(db=db, plato=plato)
```

**¿Qué hace este archivo?**
- Define los endpoints de la API
- Configura la aplicación FastAPI
- Maneja requests y responses
- Implementa inyección de dependencias

**Conceptos importantes:**
- `@router.post("/")`: Define endpoint POST
- `response_model=Plato`: Define formato de respuesta
- `db: Session = Depends(get_db)`: Inyección de dependencia
- `APIRouter`: Organiza endpoints por grupos

---

## 🔄 Cómo Funciona la API

### Flujo de una Petición POST (Crear Plato)

1. **Cliente envía petición:**
```json
POST /platos/
{
  "nombre": "Arepa",
  "precio": 50.0
}
```

2. **FastAPI recibe la petición** y la valida usando `PlatoCreate`

3. **Se inyecta la sesión de BD** usando `Depends(get_db)`

4. **Se ejecuta la función** `crear_plato()`

5. **SQLAlchemy crea el registro** en PostgreSQL

6. **Se retorna la respuesta** con el ID generado:
```json
{
  "id": 1,
  "nombre": "Arepa",
  "precio": 50.0
}
```

### Flujo de una Petición GET (Listar Platos)

1. **Cliente envía petición:** `GET /platos/`

2. **FastAPI procesa la petición**

3. **Se ejecuta** `get_platos(db)`

4. **SQLAlchemy consulta** la tabla `platos`

5. **Se retorna la lista** de platos:
```json
[
  {
    "id": 1,
    "nombre": "Arepa",
    "precio": 50.0
  },
  {
    "id": 2,
    "nombre": "Pabellón Criollo",
    "precio": 180.0
  }
]
```

---

## 📡 Endpoints Disponibles

### 🔍 GET /platos
**Descripción:** Lista todos los platos disponibles
**Respuesta:** Lista de objetos Plato
```json
[
  {
    "id": 1,
    "nombre": "Arepa",
    "precio": 50.0
  }
]
```

### 🔍 GET /platos/{plato_id}
**Descripción:** Obtiene un plato específico por ID
**Parámetros:** `plato_id` (int)
**Respuesta:** Objeto Plato
```json
{
  "id": 1,
  "nombre": "Arepa",
  "precio": 50.0
}
```

### ➕ POST /platos
**Descripción:** Crea un nuevo plato
**Body:** PlatoCreate (sin ID)
```json
{
  "nombre": "Arepa",
  "precio": 50.0
}
```
**Respuesta:** Plato creado (con ID)
```json
{
  "id": 1,
  "nombre": "Arepa",
  "precio": 50.0
}
```

### ✏️ PUT /platos/{plato_id}
**Descripción:** Actualiza un plato existente
**Parámetros:** `plato_id` (int)
**Body:** Plato completo
```json
{
  "id": 1,
  "nombre": "Arepa Reina Pepiada",
  "precio": 60.0
}
```

### 🗑️ DELETE /platos/{plato_id}
**Descripción:** Elimina un plato específico
**Parámetros:** `plato_id` (int)
**Respuesta:** 204 No Content

### 🗑️ DELETE /platos
**Descripción:** Elimina todos los platos
**Respuesta:** 204 No Content

---

## 💡 Ejemplos de Uso

### Usando la Documentación Interactiva

1. **Abre tu navegador** y ve a: `http://127.0.0.1:8000/docs`

2. **Crea un plato:**
   - Haz clic en `POST /platos`
   - Haz clic en "Try it out"
   - Ingresa el JSON:
   ```json
   {
     "nombre": "Arepa",
     "precio": 50.0
   }
   ```
   - Haz clic en "Execute"

3. **Lista los platos:**
   - Haz clic en `GET /platos`
   - Haz clic en "Try it out"
   - Haz clic en "Execute"

### Usando curl

```bash
# Crear un plato
curl -X POST "http://127.0.0.1:8000/platos/" \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Arepa", "precio": 50.0}'

# Listar platos
curl "http://127.0.0.1:8000/platos/"

# Obtener plato específico
curl "http://127.0.0.1:8000/platos/1"

# Actualizar plato
curl -X PUT "http://127.0.0.1:8000/platos/1" \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "nombre": "Arepa Reina Pepiada", "precio": 60.0}'

# Eliminar plato
curl -X DELETE "http://127.0.0.1:8000/platos/1"
```

---

## 🔄 Flujo de Datos Completo

### 1. Request → FastAPI
```
Cliente → HTTP Request → FastAPI Router
```

### 2. Validación → Pydantic
```
FastAPI → Pydantic Schema → Validación de Datos
```

### 3. Inyección → Dependencias
```
FastAPI → Dependency Injection → Database Session
```

### 4. Lógica → CRUD
```
FastAPI → CRUD Function → SQLAlchemy ORM
```

### 5. Base de Datos → PostgreSQL
```
SQLAlchemy → SQL Query → PostgreSQL
```

### 6. Response → Cliente
```
PostgreSQL → SQLAlchemy → Pydantic → FastAPI → Cliente
```

---

## ✅ Mejores Prácticas Implementadas

### 🔒 Seguridad
- ✅ Variables de entorno para datos sensibles
- ✅ Validación de datos de entrada
- ✅ Manejo seguro de conexiones de BD
- ✅ Sanitización de contraseñas en URLs

### 🏗️ Arquitectura
- ✅ Separación de responsabilidades
- ✅ Inyección de dependencias
- ✅ Patrón Repository (CRUD separado)
- ✅ Configuración centralizada

### 📝 Código Limpio
- ✅ Type hints en todas las funciones
- ✅ Documentación con docstrings
- ✅ Nombres descriptivos
- ✅ Manejo de errores apropiado

### 🚀 Rendimiento
- ✅ Conexiones de BD optimizadas
- ✅ Índices en campos importantes
- ✅ Paginación básica implementada
- ✅ Sesiones de BD con lifecycle management

---

## 🔧 Solución de Problemas

### Error: "Could not import module 'main'"
**Causa:** Problemas de importación o configuración
**Solución:**
```bash
# Verificar que estás en el directorio correcto
pwd
ls main.py

# Instalar dependencias
pip install -r requirements.txt
```

### Error: "Connection to PostgreSQL failed"
**Causa:** PostgreSQL no está corriendo o configuración incorrecta
**Solución:**
```bash
# Verificar que PostgreSQL esté corriendo
psql -U postgres -c "SELECT 1;"

# Verificar configuración en .env
cat .env
```

### Error: "UnicodeDecodeError"
**Causa:** Caracteres especiales en contraseña
**Solución:** Ya implementada con `quote_plus()` en settings.py

### Error: "Not an executable object"
**Causa:** Sintaxis SQLAlchemy incorrecta
**Solución:** Ya corregida usando `text()` para consultas SQL

### La documentación no carga
**Solución:**
```bash
# Verificar que la API esté corriendo
curl http://127.0.0.1:8000/

# Limpiar caché del navegador
# Probar en modo incógnito
```

---

## 🎓 Conceptos Clave para Aprender

### FastAPI
- **Decoradores:** `@app.get()`, `@app.post()`
- **Path Parameters:** `{plato_id}`
- **Query Parameters:** `?skip=0&limit=100`
- **Request Body:** Datos JSON
- **Response Model:** Formato de respuesta
- **Dependency Injection:** `Depends()`

### SQLAlchemy
- **Engine:** Conexión a la base de datos
- **Session:** Contexto de transacción
- **Model:** Clase que representa una tabla
- **Query:** Consultas a la base de datos
- **ORM:** Object-Relational Mapping

### Pydantic
- **BaseModel:** Clase base para esquemas
- **Field:** Configuración de campos
- **Validation:** Validación automática
- **Serialization:** Conversión de datos

### PostgreSQL
- **Database:** Colección de tablas
- **Table:** Estructura de datos
- **Primary Key:** Identificador único
- **Auto-increment:** ID automático
- **Index:** Búsquedas rápidas

---

## 🚀 Próximos Pasos

### Funcionalidades que podrías agregar:
1. **Autenticación JWT**
2. **Paginación avanzada**
3. **Filtros y búsquedas**
4. **Tests unitarios**
5. **Logging**
6. **CORS para frontend**
7. **Más modelos (Clientes, Pedidos)**
8. **Relaciones entre tablas**

### Recursos para aprender más:
- [Documentación oficial de FastAPI](https://fastapi.tiangolo.com/)
- [Documentación de SQLAlchemy](https://docs.sqlalchemy.org/)
- [Documentación de Pydantic](https://pydantic-docs.helpmanual.io/)
- [Documentación de PostgreSQL](https://www.postgresql.org/docs/)

---

## 📞 Soporte

Si tienes preguntas o problemas:
1. Revisa la sección de "Solución de Problemas"
2. Verifica la configuración de PostgreSQL
3. Revisa los logs de la aplicación
4. Consulta la documentación oficial

¡Feliz programación! 🎉 