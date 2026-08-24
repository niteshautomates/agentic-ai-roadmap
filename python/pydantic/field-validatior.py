from pydantic import BaseModel, EmailStr, Field, field_validator

class Product(BaseModel):
    name: str = Field(..., min_length=3, max_length=30)
    price: float = Field(..., gt=0)
    discount_percentage: float = Field(default=0.0, ge=0, le=100)


    @field_validator('name')
    @classmethod
    def name_must_be_capitalized(cls, v: str) -> str:
        if not v[0].isupper():
            raise ValueError('Product name must start with a capital letter')
        return v

    @field_validator('discount_percentage')
    @classmethod
    def discount_must_be_valid(cls, v: float) -> float:
        if v < 0 or v > 100:
            raise ValueError('Discount percentage must be between 0 and 100')
        return v    


# Valid instance
item = Product(name="Laptop", price=999.99, discount_percentage=101)
print(item)    