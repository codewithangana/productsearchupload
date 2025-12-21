# app/repositories/product_repo.py

from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.product import Product


def bulk_create(db: Session, products: List[Product]) -> None:
    if not products:
        return
    db.add_all(products)
    db.commit()


def list_products(db: Session, offset: int, limit: int) -> List[Product]:
    return (
        db.query(Product)
        .offset(offset)
        .limit(limit)
        .all()
    )


def search_products(
    db: Session,
    brand: Optional[str] = None,
    color: Optional[str] = None,
    min_price: Optional[int] = None,
    max_price: Optional[int] = None,
) -> List[Product]:

    query = db.query(Product)

    if brand:
        query = query.filter(Product.brand.ilike(f"%{brand}%"))

    if color:
        query = query.filter(Product.color.ilike(f"%{color}%"))

    if min_price is not None:
        query = query.filter(Product.price >= min_price)

    if max_price is not None:
        query = query.filter(Product.price <= max_price)

    return query.all()
