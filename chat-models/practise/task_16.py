from pydantic import BaseModel, Field
from typing import Optional


class Movie(BaseModel):
    title: str = Field(description="The title of the movie")
    year: int = Field(description="The year the movie was released")
    rating: Optional[float] = Field(description="The rating of the movie", default=None)

movie=Movie(title="The Matrix",year=1999)
print(movie)