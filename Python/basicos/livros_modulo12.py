from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import Optional
import secrets

app = FastAPI(
    title="API de Livros",
    description="API para gerenciar catálogo de livros.",
    version="1.0.0",
    contact={
        "name": "Lucas Machi",
        "email": "lucascolafati@gmail.com"
    }
)

MEU_USUARIO = "admin"
MINHA_SENHA = "admin123"

security = HTTPBasic()

meus_livrozinhos = {}


class Livro(BaseModel):
    nome_livro: str
    autor_livro: str
    ano_livro: int


# Essa função tem a responsabilidade de validar o usuario e senha
def autenticar_meu_usuario(credentials: HTTPBasicCredentials = Depends(security)):
    is_username_correct = secrets.compare_digest(credentials.username, MEU_USUARIO)
    is_password_correct = secrets.compare_digest(credentials.password, MINHA_SENHA)

    if not (is_username_correct and is_password_correct):
        raise HTTPException(
            status_code=401,
            detail="Usuário não autorizado! Credenciais inválidas!!!",
            headers={"WWW-Authenticate": "Basic"}
        )


@app.get("/")
def hello_world():
    return {"Hello": "World!"}


@app.get("/livros")
def get_livros(page: int = 1, limit: int = 10, credentials: HTTPBasicCredentials = Depends(autenticar_meu_usuario)):
    if page < 1 or limit < 1:
        raise HTTPException(status_code=400, detail="Page ou limit estão com valores inválidos!!!")

    if not meus_livrozinhos:
        return {"message": "Não existe nenhum livro!!"}
    
    livros_ordenados = sorted(meus_livrozinhos.items(), key = lambda x: x[0])

    start = (page - 1) * limit
    end = start + limit

    livros_paginados = [
        {"id_livro": id_livro, "nome_livro": livro_data["nome_livro"], "autor_livro": livro_data["autor_livro"], "ano_livro": livro_data["ano_livro"]}
        for id_livro, livro_data in list(meus_livrozinhos.items())[start:end]
    ]

    return {
        "page": page,
        "limit": limit,
        "total": len(meus_livrozinhos),
        "livros": livros_paginados
    }