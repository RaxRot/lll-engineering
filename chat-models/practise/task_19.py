from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel,Field
from typing import Optional

model=ChatOpenAI(model="gpt-6-luna")

class FilmInfo(BaseModel):
    """Details about a film"""
    title: str = Field(description="The title of the film")
    director: str = Field(description="The director of the film")
    release_year:int=Field(description="The release year of the film")
    genre:str=Field(description="The genre of the film")
    rating:Optional[float]=Field(description="The rating of the film",default=None)

model_with_output=model.with_structured_output(FilmInfo)
response=model_with_output.invoke("Tell me about Interstellar (2014)")
print(response)
print(response.title)
print(response.director)