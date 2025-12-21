from unittest.mock import MagicMock
from app.repositories.product_repo import bulk_create, search_products


def mock_db():
    mock_query = MagicMock()
    mock_query.filter.return_value = mock_query
    mock_query.all.return_value = []
    db = MagicMock()
    db.query.return_value = mock_query
    return db, mock_query

def test_bulk_create_with_empty_list():
    db = MagicMock()

    bulk_create(db, [])

    db.add_all.assert_not_called()
    db.commit.assert_not_called()

def test_bulk_create_with_products():
    db = MagicMock()
    products = [MagicMock(), MagicMock()]

    bulk_create(db, products)

    db.add_all.assert_called_once_with(products)
    db.commit.assert_called_once()



def test_search_brand_partial():
    db, query = mock_db()

    search_products(db, brand="stream")

    query.filter.assert_called()
    query.all.assert_called_once()


def test_search_color_partial():
    db, query = mock_db()

    search_products(db, color="bl")

    query.filter.assert_called()
    query.all.assert_called_once()


def test_search_with_brand():
    db, q = mock_db()
    search_products(db, brand="Nike")
    q.filter.assert_called()


def test_search_with_color():
    db, q = mock_db()
    search_products(db, color="Black")
    q.filter.assert_called()


def test_search_with_price_range():
    db, q = mock_db()
    search_products(db, min_price=100, max_price=500)
    assert q.filter.call_count >= 2

def test_search_all_filters_combined():
    db, query = mock_db()

    search_products(
        db,
        brand="stream",
        color="red",
        min_price=300,
        max_price=2000,
    )
def test_search_no_filters():
    db, q = mock_db()
    search_products(db)
    q.all.assert_called_once()
