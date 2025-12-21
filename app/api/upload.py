# app/api/upload.py

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.db.session import SessionLocal
from app.services.csv_parser import parse_csv
from app.services.product_service import upload_products

router = APIRouter()


@router.post("/upload")
def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed")

    db = SessionLocal()
    try:
        rows = parse_csv(file)
        valid_products, failed_rows = upload_products(db, rows)

        return {
            "stored": len(valid_products),
            "failed": failed_rows
        }
    finally:
        db.close()
