# 🚀 Instrucciones para Ejecutar la Nueva Estructura

## 📋 Pasos para Iniciar la API

### 1. **Verificar que todo esté correcto**
```bash
python test_new_structure.py
```
Deberías ver mensajes de éxito (✅) para todas las importaciones.

### 2. **Ejecutar la API**
```bash
uvicorn app.main:app --reload
```

### 3. **Acceder a la documentación**
- **Documentación interactiva:** http://127.0.0.1:8000/docs
- **Documentación alternativa:** http://127.0.0.1:8000/redoc

## 📡 Endpoints Disponibles

### **Platos (Completamente implementado)**
- `GET /api/v1/platos/` - Listar todos los platos
- `GET /api/v1/platos/{id}` - Obtener plato por ID
- `POST /api/v1/platos/` - Crear nuevo plato
- `PUT /api/v1/platos/{id}` - Actualizar plato
- `DELETE /api/v1/platos/{id}` - Eliminar plato
- `DELETE /api/v1/platos/` - Eliminar todos los platos

### **Clientes (Básico - para implementar)**
- `GET /api/v1/clientes/` - Listar clientes

### **Pedidos (Básico - para implementar)**
- `GET /api/v1/pedidos/` - Listar pedidos

## 🔧 Si hay problemas

### **Error: "No module named 'app'"**
```bash
# Asegúrate de estar en el directorio raíz del proyecto
pwd
ls app/
```

### **Error de importación**
```bash
# Verifica que todos los archivos existan
ls app/platos/
ls app/clientes/
ls app/pedidos/
```

### **Error de base de datos**
```bash
# Verifica que PostgreSQL esté corriendo
psql -U postgres -d fastapi_simple -c "SELECT 1;"
```

## 📁 Estructura Final del Proyecto

```
proyecto/
│
├── 📁 app/                          # Paquete principal
│   ├── 📄 __init__.py
│   ├── 📄 main.py                   # Punto de entrada
│   │
│   ├── 📁 platos/                   # Dominio Platos (Completo)
│   │   ├── 📄 __init__.py
│   │   ├── 📄 models.py
│   │   ├── 📄 schemas.py
│   │   ├── 📄 crud.py
│   │   └── 📄 router.py
│   │
│   ├── 📁 clientes/                 # Dominio Clientes (Básico)
│   │   ├── 📄 __init__.py
│   │   ├── 📄 models.py
│   │   └── 📄 router.py
│   │
│   └── 📁 pedidos/                  # Dominio Pedidos (Básico)
│       ├── 📄 __init__.py
│       └── 📄 router.py
│
├── 📄 database.py                   # Configuración BD
├── 📄 models.py                     # Importa todos los modelos
├── 📄 settings.py                   # Configuración
├── 📄 requirements.txt
├── 📄 test_new_structure.py         # Script de prueba
├── 📄 INSTRUCCIONES.md              # Este archivo
└── 📄 README.md                     # Documentación completa
```

## 🎯 Próximos Pasos

1. **Probar la API** con los endpoints de platos
2. **Implementar CRUD completo** para clientes
3. **Implementar CRUD completo** para pedidos
4. **Agregar relaciones** entre modelos
5. **Implementar autenticación**

¡La nueva estructura está lista para usar! 🎉 