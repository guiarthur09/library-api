from database.connection import connection, cursor
from models.books import BookCreate, Book
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/")
def home():
    return {
        "mensagem": "Bem-vindo à API da Biblioteca!"
    }

@router.post("/books", response_model=Book)
def criar_livro(livro: BookCreate):

    cursor.execute("""INSERT INTO books (title, author, publisher, location, year, pages)
    VALUES (?, ?, ?, ?, ?, ?)""", (livro.title, livro.author, livro.publisher, livro.location, livro.year, livro.pages))

    connection.commit()

    novo_id = cursor.lastrowid
    return {**livro.model_dump(), "id": novo_id}

@router.get("/books")
def listar_livros():

    cursor.execute("""SELECT * FROM books""")

    livros = cursor.fetchall()
    return [dict(livro) for livro in livros]


@router.get("/books/{id}")
def buscar_livro(id: int):

   cursor.execute("""SELECT * FROM books WHERE id= ?""", (id,))

   livro = cursor.fetchone()
   if livro:
       return dict(livro)

   raise HTTPException(status_code=404, detail="404 Not Found")

@router.put("/books/{id}", response_model=Book)
def atualizar_livro(id: int, livro: BookCreate):

    cursor.execute("""UPDATE books
                      SET title=?, author=?,
                      publisher=?, location=?,
                      year=?, pages=?
                      WHERE id=?""", (livro.title, livro.author, livro.publisher, livro.location, livro.year, livro.pages, id))

    connection.commit()

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="404 Not Found")

    return {**livro.model_dump(), "id": id}

@router.delete("/books/{id}")
def deletar_livro(id: int):

    cursor.execute("""DELETE FROM books WHERE id=?""", (id,))
    connection.commit()

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="404 Not Found")

    return {"deleted": f"ID: {id}"}
