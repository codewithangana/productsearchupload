# app/schemas/product.py

from pydantic import BaseModel
from typing import Optional


class ProductBase(BaseModel):
    sku: str
    name: str
    brand: str
    color: Optional[str] = None
    size: Optional[str] = None
    mrp: int
    price: int
    quantity: int


class ProductResponse(ProductBase):
    class Config:
        orm_mode = True
