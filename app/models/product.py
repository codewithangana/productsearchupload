# app/models/product.py

from sqlalchemy import Column, Integer, String

from app.db.base import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    sku = Column(String(100), unique=True, nullable=False, index=True)
    name = Column(String(255), nullable=False)
    brand = Column(String(100), nullable=False, index=True)

    color = Column(String(50))
    size = Column(String(50))

    mrp = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False, default=0)
