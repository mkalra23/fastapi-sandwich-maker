from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base
import datetime

# Sandwiches Table
class Sandwich(Base):
    __tablename__ = "sandwiches"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    price = Column(Float)

    recipes = relationship("Recipe", back_populates="sandwich")
    orders = relationship("OrderDetail", back_populates="sandwich")


# Resources Table
class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    quantity = Column(Integer)

    recipes = relationship("Recipe", back_populates="resource")


# Recipes Table
class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))
    resource_id = Column(Integer, ForeignKey("resources.id"))
    quantity = Column(Integer)

    sandwich = relationship("Sandwich", back_populates="recipes")
    resource = relationship("Resource", back_populates="recipes")


# OrderDetails Table
class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True)
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))
    order_time = Column(DateTime, default=datetime.datetime.utcnow)
    customer_name = Column(String)

    sandwich = relationship("Sandwich", back_populates="orders")


