from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel,Field
from typing import Optional

model=ChatOpenAI(model="gpt-6-luna")

class CountryInfo(BaseModel):
    """Details about a country"""
    name: str = Field(description="The name of the country")
    capital: str = Field(description="The capital of the country")
    population: int = Field(description="The population of the country")
    currency:Optional[str]=Field(description="The currency of the country",default=None)

model_with_output=model.with_structured_output(CountryInfo)
response=model_with_output.invoke("Tell me about Japan.")
print(response)
print(response.name)
print(response.capital)
print(response.population)