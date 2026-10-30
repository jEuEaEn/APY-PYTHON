from fastapi import FastAPI, HTTPException, status
from pydantic import Field, BaseModel 

app = FastAPI(

    title= "Apy python products(App)",
    description="Apy para administrativo de productos",
    version="1.0.0"
)


class EntradaProductos(BaseModel):
    nombre: str = Field(min_length= 3, max_length= 50)
    precio: float = Field(gt=0)
    descripcion: str = ""

productos = [
    {
        "id": 1,
        "nombre": "Teclado",
        "precio": 75000,
        "descripcion": "Teclado USB"
    },
    {
        "id": 2,
        "nombre": "Mouse",
        "precio": 35000,
        "descripcion": "Mouse optico"
    },
    {
        "id": 3,
        "nombre": "Monitor",
        "precio": 520000,
        "descripcion": "Monitor de 24 pulgadas"
    }
]

#Verificar que el servidor sirva
@app.get("/")
def inicio():
    return{
        "mensaje": "WELCOME to API Rest for Products XD",
        "estado": "Servidor operativo"
    }

# Obtener productos
@app.get("/productos")
def listaProductos():
    return productos

# Selecionar productos por id
@app.get("/productos/{id}")
def buscarProducto(id: int):
    
    for producto in productos:
        if producto["id"] == id:
            return producto

    raise HTTPException(
        status_code=404,
        detail="Producto no encontrado"
    )

# POST de productos
@app.post("/productos", status_code=status.HTTP_201_CREATED)
def crearProducto(entrada: EntradaProductos):

    nuevoProducto = {
        "id": max((p["id"] for p in productos), default= 0) + 1,
        "nombre": entrada.nombre,
        "precio": entrada.precio,
        "descripcion": entrada.descripcion
    }

    productos.append(nuevoProducto)

    return{
        "mensaje": "Producto creado correctamente",
        "producto": nuevoProducto
    }


#DELETE
@app.delete("/productos/{id}")
def eliminarProducto(id: int):

    for producto in productos:
        if producto["id"] == id:
            productos.remove(producto)
            return{
                "mensaje": "Producto Eliminado correctamente",
                "producto": producto
            }

    raise HTTPException(

        status_code=404,
        detail="producto no encontrado"

    )