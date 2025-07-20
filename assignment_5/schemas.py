from pydantic import BaseModel
from datetime import datetime

# ===== Sandwich =====
class SandwichBase(BaseModel):
    name: str
    price: float

class SandwichCreate(SandwichBase):
    pass

class Sandwich(SandwichBase):
    id: int

    model_config = {
        "from_attributes": True
}

# ===== Resource =====
class ResourceBase(BaseModel):
    name: str
    quantity: int

class ResourceCreate(ResourceBase):
    pass

class Resource(ResourceBase):
    id: int

    class Config:
        orm_mode = True


# ===== Recipe =====
class RecipeBase(BaseModel):
    sandwich_id: int
    resource_id: int
    quantity: int

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int

    class Config:
        orm_mode = True


# ===== Order Detail =====
class OrderDetailBase(BaseModel):
    sandwich_id: int
    customer_name: str

class OrderDetailCreate(OrderDetailBase):
    pass

class OrderDetail(OrderDetailBase):
    id: int
    order_time: datetime

    class Config:
        orm_mode = True

