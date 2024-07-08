from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import List, Dict
from .base import Storage
from ..models.models import Base, Product, ProductSchema

DATABASE_URL = "sqlite:///./scraped_data.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class SQLiteStorage(Storage):
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = SessionLocal()

    def save(self, data: List[Dict]) -> int:
        updated_count = 0
        for item in data:
            db_product = self.db.query(Product).filter(Product.product_title == item["product_title"]).first()
            if db_product:
                if db_product.product_price != item["product_price"]:
                    db_product.product_price = item["product_price"]
                    db_product.path_to_image = item["path_to_image"]
                    self.db.commit()
                    updated_count += 1
            else:
                new_product = Product(
                    product_title=item["product_title"],
                    product_price=item["product_price"],
                    path_to_image=item["path_to_image"]
                )
                self.db.add(new_product)
                self.db.commit()
                updated_count += 1
        return updated_count

    def load(self) -> List[ProductSchema]:
        return self.db.query(Product).all()
