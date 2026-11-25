from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel,Field
from typing import Optional

model=ChatOpenAI(model="gpt-6-luna")
 
class President(BaseModel):
    """Details about the president of a country"""
    name: str = Field(description="The name of the president")
    country:str=Field(description="The country of the president")
    age:Optional[int]=Field(description="The age of the president",default=None)


structured_llm=model.with_structured_output(President)
response=structured_llm.invoke("Who is the president of USA?")
print(response)