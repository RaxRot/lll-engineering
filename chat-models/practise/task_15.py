from pydantic import BaseModel,Field

class Book(BaseModel):
    title: str = Field(description="The title of the book")
    author: str = Field(description="The author of the book")
    pages: int = Field(description="The number of pages in the book")

book=Book(title="Harry Potter",author="J.K. Rowling",pages=350)
print(book)