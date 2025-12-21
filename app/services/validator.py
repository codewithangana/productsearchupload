# app/services/validator.py

from typing import Dict, Tuple, Optional


REQUIRED_FIELDS = ["sku", "name", "brand", "mrp", "price"]


def validate_row(row: Dict) -> Tuple[bool, Optional[str]]:
    """
    Validate a single product row parsed from CSV.
    Returns: (is_valid, error_message)
    """

    # Required fields check
    for field in REQUIRED_FIELDS:
        if field not in row or row[field] in (None, ""):
            return False, f"{field} is required"

    # Type & value checks
    try:
        mrp = int(row["mrp"])
        price = int(row["price"])
        quantity = int(row.get("quantity", 0))
    except ValueError:
        return False, "Invalid number format"

    if price > mrp:
        return False, "price cannot be greater than mrp"

    if quantity < 0:
        return False, "quantity cannot be negative"

    return True, None
