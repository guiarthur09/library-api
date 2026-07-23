from pydantic import BaseModel

class LivroCreate(BaseModel):
    titulo: str
    autor: str

class Livro(BaseModel):
    id: int
    titulo: str
    autor: str