from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel,Field
from typing import Optional

model=ChatOpenAI(model="gpt-6-luna")

class Product(BaseModel):
    """Details about a product"""
    name: str = Field(description="The name of the product")
    price: float = Field(description="The price of the product")
    quantity:int=Field(description="The quantity of the product")
    description:Optional[str]=Field(description="The description of the product",default=None)

product=Product(name="Laptop",price=999.99,quantity=2)
print(product)
print(product.price)
print(product.description)

