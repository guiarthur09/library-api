from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# Modelo que representa os dados que o usuário envia
class LivroCreate(BaseModel):
    titulo: str
    autor: str


# Modelo que representa um livro completo
class Livro(BaseModel):
    id: int
    titulo: str
    autor: str


livros = [
    {
        "id": 1,
        "titulo": "Python para Iniciantes",
        "autor": "João Silva"
    },
    {
        "id": 2,
        "titulo": "FastAPI na Prática",
        "autor": "Maria Souza"
    },
    {
        "id": 3,
        "titulo": "Banco de Dados",
        "autor": "Carlos Lima"
    }
]

@app.get("/")
def home():
    return {
        "mensagem": "Bem-vindo à API da Biblioteca!"
    }

@app.post("/books")
def criar_livro(livro: LivroCreate):

    novo_id = len(livros) + 1

    novo_livro = {
        "id": novo_id,
        "titulo": livro.titulo,
        "autor": livro.autor
    }

    livros.append(novo_livro)

    return novo_livro

@app.get("/books")
def listar_livros():
    return livros


@app.get("/books/{id}")
def buscar_livro(id: int):
    for livro in livros:
        if livro["id"] == id:
            return livro
    raise HTTPException(status_code=404, detail="404 Not Found")
        
        