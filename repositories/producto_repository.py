from interfaces.producto_repository_interface import ProductoRepositoryInterface


class ProductoRepository(ProductoRepositoryInterface):

    def __init__(self):
        self.__productos = []
        self.__siguiente_id = 1

    def obtener_todos(self):
        return self.__productos

    def obtener_por_id(self, id):
        for producto in self.__productos:
            if producto.id == id:
                return producto
        return None

    def crear(self, producto):
        producto.id = self.__siguiente_id
        self.__siguiente_id += 1
        self.__productos.append(producto)
        return producto

    def actualizar(self, producto):
        existente = self.obtener_por_id(producto.id)

        if existente is None:
            return None

        existente.nombre = producto.nombre
        existente.precio = producto.precio
        existente.categoria = producto.categoria
        existente.stock = producto.stock

        return existente

    def eliminar(self, id):
        producto = self.obtener_por_id(id)

        if producto is None:
            return False

        self.__productos.remove(producto)
        return True
