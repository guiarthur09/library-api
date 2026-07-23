from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    publisher: str
    location: str
    year: int
    pages: int

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    location: str
    year: int
    pages: int
