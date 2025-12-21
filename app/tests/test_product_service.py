from app.services.product_service import upload_products


def test_upload_products(mocker):
    # IMPORTANT: mock where it is USED, not where it is defined
    mocker.patch("app.services.product_service.bulk_create")

    rows = [
        {
            "sku": "A1",
            "name": "Good",
            "brand": "BrandX",
            "mrp": "1000",
            "price": "500",
            "quantity": "10",
        },
        {
            "sku": "A2",
            "name": "Bad",
            "brand": "BrandX",
            "mrp": "500",
            "price": "1000",
            "quantity": "1",
        },
    ]

    valid, failed = upload_products(None, rows)

    assert len(valid) == 1
    assert len(failed) == 1
    assert failed[0]["sku"] == "A2"
