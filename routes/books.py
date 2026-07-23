from models.books import LivroCreate, Livro
from fastapi import APIRouter, HTTPException

router = APIRouter()

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

@router.get("/")
def home():
    return {
        "mensagem": "Bem-vindo à API da Biblioteca!"
    }

@router.post("/books", response_model=Livro)
def criar_livro(livro: LivroCreate):

    novo_id = len(livros) + 1

    novo_livro = {
        "id": novo_id,
        "titulo": livro.titulo,
        "autor": livro.autor
    }

    livros.append(novo_livro)

    return novo_livro

@router.get("/books")
def listar_livros():
    return livros


@router.get("/books/{id}")
def buscar_livro(id: int):
    for livro in livros:
        if livro["id"] == id:
            return livro
    raise HTTPException(status_code=404, detail="404 Not Found")

@router.put("/books/{id}", response_model=Livro)
def atualizar_livro(id: int, livro_atualizado: LivroCreate):
    for livro in livros:
        if livro["id"] == id:
            livro["titulo"] = livro_atualizado.titulo
            livro["autor"] = livro_atualizado.autor
            return livro

    raise HTTPException(status_code=404, detail="404 Not Found")

@router.delete("/books/{id}")
def deletar_livro(id: int):
    for index, livro in enumerate(livros):
        if livro["id"] == id:
            del livros[index]
            return {"deleted": f"ID: {livro['id']} | Name: {livro['titulo']} | Autor: {livro['autor']}"}
        
    raise HTTPException(status_code=404, detail="404 Not Found")
