from db.session import engine
from db.base import Base
from models.product import Product



print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done!")
