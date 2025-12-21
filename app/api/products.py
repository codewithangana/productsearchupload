# app/api/products.py

from typing import List, Optional

from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

from app.db.session import SessionLocal
from app.repositories.product_repo import list_products, search_products
from app.schemas.product import ProductResponse

router = APIRouter()


@router.get("/products", response_model=List[ProductResponse])
def get_products(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
):
    offset = (page - 1) * limit
    db = SessionLocal()
    try:
        return list_products(db, offset, limit)
    finally:
        db.close()



@router.get("/products/search", response_model=List[ProductResponse])
def search(
    brand: Optional[str] = None,
    color: Optional[str] = None,
    minPrice: Optional[int] = Query(None, ge=0),
    maxPrice: Optional[int] = Query(None, ge=0),
):
    db = SessionLocal()
    try:
        results = search_products(
            db,
            brand=brand,
            color=color,
            min_price=minPrice,
            max_price=maxPrice,
        )
        if not results:
            return JSONResponse(
                status_code=200,
                content={
                    "message": "No data found in database",
                    "data": []
                }
            )
        return results
    finally:
        db.close()        
