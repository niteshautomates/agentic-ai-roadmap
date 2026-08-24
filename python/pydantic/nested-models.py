from typing import List
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class Order(BaseModel):
    order_id: str
    customer_name: str
    shipping_address: Address
    items: List[str]




raw_data = {
    "order_id" : "ORD-34535",
    "customer_name" : "John Doe",
    "items" : ["MacBook Pro M5", "Keyboards", "Mouse"],
    "shipping_address" : { "city": "New York" , "state": "NY", "street": "123 Main St", "zip_code": "10001"}
    }

order = Order(**raw_data)
print(order.model_dump_json())