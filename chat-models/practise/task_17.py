from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel,Field
from typing import Optional

model=ChatOpenAI(model="gpt-6-luna")

class Animal(BaseModel):
    """Details about an animal"""
    name: str = Field(description="The name of the animal")
    habitat: str = Field(description="The habitat of the animal")
    lifespan:Optional[int]=Field(description="The lifespan of the animal",default=None)

structured_llm=model.with_structured_output(Animal)
response=structured_llm.invoke("polar bear")
print(response)
print(response.name)
print(response.habitat)