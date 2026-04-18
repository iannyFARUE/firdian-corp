from pydantic import BaseModel, Field

from typing import List, Optional, Dict

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True
    discount: float = Field(
        ..., ge=0, le=100, description="Discount percentage for the product", examples=10.0
    )

class Cart(BaseModel):
    user_id: int
    items: List[Product]
    quantity: Dict[int, int]  # product_id to quantity mapping
    
if __name__ == "__main__":
    p1 = Product(id=1, name='Laptop', price=999.99, in_stock=True, discount=10.0)
    print(p1)

    p2 = Product(id=4,name='Smartphone', price=499.99, discount=5.0)
    print(p2)

    cart = Cart(user_id=1, items=[p1, p2], quantity={1: 1, 4: 2})
    print(cart)