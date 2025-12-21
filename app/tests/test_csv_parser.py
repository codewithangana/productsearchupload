from io import BytesIO
from fastapi import UploadFile

from app.services.csv_parser import parse_csv


def test_parse_csv():
    csv_content = (
        "sku,name,brand,mrp,price,quantity\n"
        "A1,Shirt,BrandX,1000,500,10\n"
    ).encode("utf-8")

    file = UploadFile(
        filename="test.csv",
        file=BytesIO(csv_content),
    )

    rows = parse_csv(file)

    assert len(rows) == 1
    assert rows[0]["sku"] == "A1"
    assert rows[0]["price"] == "500"
