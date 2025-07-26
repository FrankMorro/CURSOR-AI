# API FastAPI con PostgreSQL - Guía Completa

## 📋 Tabla de Contenidos
1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Tecnologías Utilizadas](#tecnologías-utilizadas)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Conceptos Básicos](#conceptos-básicos)
5. [Configuración Inicial](#configuración-inicial)
6. [Explicación Detallada de la Estructura por Dominios](#explicación-detallada-de-la-estructura-por-dominios)
7. [Cómo Funciona la API](#cómo-funciona-la-api)
8. [Endpoints Disponibles](#endpoints-disponibles)
9. [Ejemplos de Uso](#ejemplos-de-uso)
10. [Flujo de Datos](#flujo-de-datos)
11. [Mejores Prácticas Implementadas](#mejores-prácticas-implementadas)
12. [Solución de Problemas](#solución-de-problemas)

---

## 🎯 Descripción del Proyecto

Esta es una API REST completa construida con **FastAPI** y **PostgreSQL** que implementa un sistema de gestión de platos, clientes y pedidos. La arquitectura está basada en dominios, separando la lógica de cada entidad en carpetas independientes para mayor escalabilidad y mantenibilidad.

### ¿Qué hace esta API?

- ✅ Gestiona platos, clientes y pedidos
- ✅ Almacena datos en PostgreSQL
- ✅ Genera IDs automáticamente
- ✅ Valida datos de entrada
- ✅ Maneja errores apropiadamente
- ✅ Genera documentación automática
- ✅ Estructura modular basada en dominios

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
CURSOR-AI/
│
├── app/
│   ├── __init__.py
│   ├── main.py                # Punto de entrada FastAPI
│   ├── clientes/              # Dominio Clientes
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── router.py
│   ├── platos/                # Dominio Platos
│   │   ├── __init__.py
│   │   ├── crud.py
│   │   ├── models.py
│   │   ├── router.py
│   │   ├── schemas.py
│   ├── pedidos/               # Dominio Pedidos
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── router.py
│
├── database.py                # Configuración de la base de datos
├── models.py                  # Importa y expone todos los modelos
├── settings.py                # Configuración y variables de entorno
├── requirements.txt           # Dependencias del proyecto
├── test_new_structure.py      # Script para probar la estructura
├── test_paginacion_platos.py  # Script para probar paginación
└── README.md                  # Esta documentación
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
uvicorn app.main:app --reload
```

---

## 🏗️ Explicación Detallada de la Estructura por Dominios

La carpeta `app/` contiene un subdirectorio para cada dominio principal del sistema (platos, clientes, pedidos). Cada dominio tiene su propio archivo de modelos, router y (si aplica) schemas y crud. Esto permite escalar el proyecto fácilmente y mantener el código organizado.

- **app/platos/**: Lógica y endpoints para platos
  - `models.py`: Modelo SQLAlchemy del plato
  - `schemas.py`: Esquemas Pydantic para validación
  - `crud.py`: Operaciones CRUD para platos
  - `router.py`: Endpoints de la API para platos
- **app/clientes/**: Lógica y endpoints para clientes
  - `models.py`: Modelo SQLAlchemy del cliente
  - `router.py`: Endpoints de la API para clientes
- **app/pedidos/**: Lógica y endpoints para pedidos
  - `models.py`: Modelo SQLAlchemy del pedido
  - `router.py`: Endpoints de la API para pedidos
- **main.py**: Incluye los routers de cada dominio en la aplicación principal

**Ventajas de la estructura por dominios:**

- Escalabilidad: fácil agregar nuevos dominios
- Separación de responsabilidades
- Mejor mantenibilidad
- Código más limpio y modular

---

## 🔄 Cómo Funciona la API

1. El cliente realiza una petición HTTP a un endpoint de dominio (por ejemplo, `/platos/`).
2. FastAPI valida los datos usando los esquemas Pydantic del dominio.
3. Se inyecta la sesión de base de datos usando `Depends(get_db)`.
4. Se ejecuta la función CRUD correspondiente del dominio.
5. SQLAlchemy realiza la operación en la base de datos.
6. Se retorna la respuesta al cliente.

---

## 📡 Endpoints Disponibles

### 🔍 GET /platos

**Descripción:** Lista todos los platos disponibles con paginación avanzada
**Parámetros de consulta:**

- `skip`: Registros a omitir (offset)
- `limit`: Cantidad de registros por página
**Respuesta:**

```json
{
  "total": 20,
  "page": 2,
  "per_page": 5,
  "total_pages": 4,
  "has_next": true,
  "has_prev": true,
  "items": [
    { "id": 6, "nombre": "Arepa", "precio": 50.0 },
    ...
  ]
}
```

### 🔍 GET /platos/{plato_id}

**Descripción:** Obtiene un plato específico por ID
**Respuesta:**

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
**Respuesta:** 204 No Content

---

## 💡 Ejemplos de Uso

### Usando la Documentación Interactiva

1. **Abre tu navegador** y ve a: `http://127.0.0.1:8000/docs`
2. Prueba los endpoints de cada dominio (platos, clientes, pedidos)

### Usando curl

```bash
# Crear un plato
curl -X POST "http://127.0.0.1:8000/platos/" \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Arepa", "precio": 50.0}'

# Listar platos (paginado)
curl "http://127.0.0.1:8000/platos/?skip=5&limit=5"

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

``` txt
Cliente → HTTP Request → FastAPI Router
```

### 2. Validación → Pydantic

``` txt
FastAPI → Pydantic Schema → Validación de Datos
```

### 3. Inyección → Dependencias

``` txt
FastAPI → Dependency Injection → Database Session
```

### 4. Lógica → CRUD

``` txt
FastAPI → CRUD Function → SQLAlchemy ORM
```

### 5. Base de Datos → PostgreSQL

``` txt
SQLAlchemy → SQL Query → PostgreSQL
```

### 6. Response → Cliente

``` txt
PostgreSQL → SQLAlchemy → Pydantic → FastAPI → Cliente
```

---

## ✅ Mejores Prácticas Implementadas

- Estructura modular basada en dominios
- Separación de responsabilidades
- Inyección de dependencias
- Validación de datos con Pydantic
- Manejo seguro de sesiones de base de datos
- Documentación automática con OpenAPI/Swagger
- Paginación avanzada en endpoints de listado

---

## 🔧 Solución de Problemas

- Verifica que la base de datos esté corriendo y la configuración en `.env` sea correcta.
- Usa los scripts de prueba (`test_new_structure.py`, `test_paginacion_platos.py`) para validar la estructura y la paginación.
- Consulta la documentación oficial de FastAPI, SQLAlchemy y Pydantic para dudas avanzadas.

---

¡Feliz programación y disfruta tu API modular! 🎉
