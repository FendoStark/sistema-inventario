from fastapi import APIRouter, Depends, HTTPException, status

from repositories.producto_repository import ProductoRepository
from services.producto_service import ProductoService
from schemas.producto_schema import ProductoCreate, ProductoResponse


router = APIRouter(
    prefix="/api/productos",
    tags=["Productos"]
)

repository = ProductoRepository()


def get_producto_service():
    return ProductoService(repository)


@router.get("", response_model=list[ProductoResponse])
def listar_productos(
    service: ProductoService = Depends(get_producto_service)
):
    productos = service.obtener_productos()
    return [producto.to_dict() for producto in productos]


@router.get("/{id}", response_model=ProductoResponse)
def obtener_producto(
    id: int,
    service: ProductoService = Depends(get_producto_service)
):
    producto = service.obtener_producto(id)

    if producto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado"
        )

    return producto.to_dict()


@router.post(
    "",
    response_model=ProductoResponse,
    status_code=status.HTTP_201_CREATED
)
def crear_producto(
    datos: ProductoCreate,
    service: ProductoService = Depends(get_producto_service)
):
    producto = service.crear_producto(datos)
    return producto.to_dict()


@router.put("/{id}", response_model=ProductoResponse)
def actualizar_producto(
    id: int,
    datos: ProductoCreate,
    service: ProductoService = Depends(get_producto_service)
):
    producto = service.actualizar_producto(id, datos)

    if producto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado"
        )

    return producto.to_dict()


@router.delete("/{id}")
def eliminar_producto(
    id: int,
    service: ProductoService = Depends(get_producto_service)
):
    eliminado = service.eliminar_producto(id)

    if not eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado"
        )

    return {"mensaje": "Producto eliminado correctamente"}
