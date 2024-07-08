from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_title = Column(String, unique=True, nullable=False)
    product_price = Column(Float, nullable=False)
    path_to_image = Column(String, nullable=False)

class ProductSchema(BaseModel):
    product_title: str
    product_price: float
    path_to_image: str

