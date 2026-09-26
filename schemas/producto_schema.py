from pydantic import BaseModel, Field


class ProductoCreate(BaseModel):
    nombre: str = Field(min_length=2)
    precio: float = Field(ge=0)
    categoria: str = Field(min_length=1)
    stock: int = Field(ge=0)


class ProductoResponse(BaseModel):
    id: int
    nombre: str
    precio: float
    categoria: str
    stock: int
