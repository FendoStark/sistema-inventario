class Producto:
    def __init__(self, id, nombre, precio, categoria, stock):
        self.__id = id
        self.__nombre = nombre
        self.__precio = precio
        self.__categoria = categoria
        self.__stock = stock

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, valor):
        self.__id = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        self.__precio = valor

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, valor):
        self.__categoria = valor

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, valor):
        self.__stock = valor

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria,
            "stock": self.stock
        }
