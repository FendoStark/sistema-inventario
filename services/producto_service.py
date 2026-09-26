from models.producto import Producto


class ProductoService:

    def __init__(self, repository):
        self.__repository = repository

    def obtener_productos(self):
        return self.__repository.obtener_todos()

    def obtener_producto(self, id):
        return self.__repository.obtener_por_id(id)

    def crear_producto(self, datos):
        producto = Producto(
            None,
            datos.nombre,
            datos.precio,
            datos.categoria,
            datos.stock
        )

        return self.__repository.crear(producto)

    def actualizar_producto(self, id, datos):
        producto = Producto(
            id,
            datos.nombre,
            datos.precio,
            datos.categoria,
            datos.stock
        )

        return self.__repository.actualizar(producto)

    def eliminar_producto(self, id):
        return self.__repository.eliminar(id)
