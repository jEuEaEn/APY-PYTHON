
# API REST de Productos con FastAPI

## 1. Descripción
Este proyecto consiste en una API REST desarrollada con Python y FastAPI, que permite administrar productos mediante solicitudes HTTP.

La API permite consultar, registrar, buscar y eliminar productos. La información se almacena temporalmente en una lista de Python.

## 2. Tecnologías utilizadas
- Python
- FastAPI
- Uvicorn
- Pydantic

## 3. Instalación

Primero, es necesario tener Python instalado.

Después, abrir una terminal en la carpeta del proyecto y ejecutar:

```bash
pip install fastapi uvicorn
```

## 4. Ejecución del servidor

Para iniciar el servidor, ejecutar el siguiente comando:

```bash
uvicorn main:app --reload
```

El servidor estará disponible en:

http://127.0.0.1:8000

## 5. Endpoints disponibles

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | / | Muestra el estado del servidor |
| GET | /productos | Lista todos los productos |
| GET | /productos/{id} | Busca un producto por su ID |
| POST | /productos | Registra un producto nuevo |
| DELETE | /productos/{id} | Elimina un producto |

## 6. Ejemplos de solicitudes

### GET /
Consulta el estado del servidor.

URL:
http://127.0.0.1:8000/

### GET /productos
Obtiene todos los productos registrados.

URL:
http://127.0.0.1:8000/productos

### GET /productos/{id}
Busca un producto por su identificador.

Ejemplo:
http://127.0.0.1:8000/productos/1

### POST /productos
Registra un producto nuevo.

URL:
http://127.0.0.1:8000/productos

Cuerpo JSON:

```json
{
    "nombre": "Audifonos",
    "precio": 120000,
    "descripcion": "Audifonos Bluetooth"
}
```

### DELETE /productos/{id}
Elimina un producto utilizando su identificador.

Ejemplo:
http://127.0.0.1:8000/productos/2

## 7. Códigos de estado HTTP

- 200: Solicitud realizada correctamente.
- 201: Producto creado correctamente.
- 404: Producto no encontrado.
- 422: Datos enviados incorrectamente.

## 8. Documentación y pruebas

FastAPI proporciona una documentación interactiva que permite probar todos los endpoints sin necesidad de instalar herramientas adicionales.

Para acceder, ingresar a:

http://127.0.0.1:8000/docs

Desde allí se pueden ejecutar solicitudes GET, POST y DELETE.

## 9. Almacenamiento de datos

Los productos se guardan en una lista de Python. No se utiliza una base de datos, por lo que los cambios realizados se pierden cuando se reinicia el servidor.

## 10. Autor
Proyecto académico: Creación de una API REST con Python y FastAPI.
