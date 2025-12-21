from app.services.validator import validate_row


def test_valid_row():
    row = {
        "sku": "A1",
        "name": "Shirt",
        "brand": "BrandX",
        "mrp": "1000",
        "price": "500",
        "quantity": "10",
    }

    is_valid, error = validate_row(row)

    assert is_valid is True
    assert error is None


def test_price_greater_than_mrp():
    row = {
        "sku": "A2",
        "name": "Bad Shirt",
        "brand": "BrandX",
        "mrp": "500",
        "price": "1000",
        "quantity": "1",
    }

    is_valid, error = validate_row(row)

    assert is_valid is False
    assert error == "price cannot be greater than mrp"


def test_negative_quantity():
    row = {
        "sku": "A3",
        "name": "Bad Qty",
        "brand": "BrandX",
        "mrp": "1000",
        "price": "500",
        "quantity": "-5",
    }

    is_valid, error = validate_row(row)

    assert is_valid is False
    assert error == "quantity cannot be negative"


def test_missing_required_field():
    row = {
        "sku": "A4",
        "brand": "BrandX",
        "mrp": "1000",
        "price": "500",
    }

    is_valid, error = validate_row(row)

    assert is_valid is False
    assert "is required" in error


def test_invalid_number_format():
    row = {
        "sku": "A5",
        "name": "Invalid Number",
        "brand": "BrandX",
        "mrp": "abc",
        "price": "500",
        "quantity": "10",
    }

    is_valid, error = validate_row(row)

    assert is_valid is False
    assert error == "Invalid number format"
