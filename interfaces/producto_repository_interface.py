from abc import ABC, abstractmethod


class ProductoRepositoryInterface(ABC):

    @abstractmethod
    def obtener_todos(self):
        pass

    @abstractmethod
    def obtener_por_id(self, id):
        pass

    @abstractmethod
    def crear(self, producto):
        pass

    @abstractmethod
    def actualizar(self, producto):
        pass

    @abstractmethod
    def eliminar(self, id):
        pass
