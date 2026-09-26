# Sistema de Gestión de Productos

Proyecto académico de sistema web Full-Stack para demostrar **CRUD, POO y principios SOLID** con Python y FastAPI.

## Tecnologías

- Python
- FastAPI
- Uvicorn
- Pydantic
- HTML5
- CSS3
- JavaScript

## Arquitectura

```text
Frontend (HTML + CSS + JS)
            ↓
         FastAPI
            ↓
       Controller
            ↓
         Service
            ↓
   Repository Interface
            ↓
        Repository
            ↓
     Datos en memoria
```

## Estructura

```text
models/          Entidades y POO
schemas/         Validación de datos con Pydantic
interfaces/      Abstracciones del repositorio
repositories/    Persistencia en memoria
services/        Lógica de negocio
controllers/     Endpoints REST
templates/       Interfaz HTML
static/          CSS y JavaScript
```

## Instalación

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecutar

```bash
uvicorn main:app --reload
```

Abrir en el navegador:

http://127.0.0.1:8000

## Documentación de la API

Swagger UI:

http://127.0.0.1:8000/docs

ReDoc:

http://127.0.0.1:8000/redoc

## CRUD

| Método | Endpoint | Operación |
|---|---|---|
| GET | `/api/productos` | Listar |
| GET | `/api/productos/{id}` | Buscar por ID |
| POST | `/api/productos` | Crear |
| PUT | `/api/productos/{id}` | Actualizar |
| DELETE | `/api/productos/{id}` | Eliminar |

## POO

La clase `Producto` utiliza atributos encapsulados y propiedades para controlar el acceso a sus datos.

## SOLID

- **S — Responsabilidad Única:** cada capa tiene una responsabilidad concreta.
- **O — Abierto/Cerrado:** las responsabilidades están separadas y el acceso a persistencia se realiza mediante una abstracción.
- **D — Inversión de Dependencias:** `ProductoService` recibe un repositorio y el Controller obtiene el servicio mediante `Depends`.

## Persistencia

La evaluación indica que la base de datos no es obligatoria, por lo que esta versión utiliza una colección en memoria. Los datos se pierden al reiniciar el servidor.
