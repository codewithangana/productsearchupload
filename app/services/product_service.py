# app/services/product_service.py

from typing import List, Dict, Tuple

from sqlalchemy.orm import Session

from app.models.product import Product
from app.repositories.product_repo import bulk_create
from app.services.validator import validate_row


def upload_products(
    db: Session,
    rows: List[Dict]
) -> Tuple[List[Product], List[Dict]]:
    """
    Validate CSV rows and store valid products.
    Returns: (valid_products, failed_rows)
    """

    valid_products: List[Product] = []
    failed_rows: List[Dict] = []

    for row in rows:
        is_valid, error = validate_row(row)

        if not is_valid:
            failed_rows.append({
                "sku": row.get("sku"),
                "reason": error
            })
            continue

        product = Product(
            sku=row["sku"],
            name=row["name"],
            brand=row["brand"],
            color=row.get("color"),
            size=row.get("size"),
            mrp=int(row["mrp"]),
            price=int(row["price"]),
            quantity=int(row.get("quantity", 0)),
        )

        valid_products.append(product)

    bulk_create(db, valid_products)

    return valid_products, failed_rows
