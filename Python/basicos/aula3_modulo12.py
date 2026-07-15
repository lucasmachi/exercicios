from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import Optional
import secrets
import os

#validação automatica usando pydantic

app = FastAPI()

tarefas = []

MEU_USUARIO = "admin"
MINHA_SENHA =  "admin"

security = HTTPBasic()

class Tarefa(BaseModel):
    nome: str
    descricao: str

def autenticar_usuario(credentials: HTTPBasicCredentials = Depends(security)):
    is_user_correct = secrets.compare_digest(credentials.username, MEU_USUARIO)
    is_password_correct = secrets.compare_digest(credentials.password, MINHA_SENHA)
    
    if not (is_user_correct and is_password_correct):
        raise HTTPException (
            status_code=401,
            detail="Usuário ou senha inválidos",
            headers={"WWW-Authenticate": "Basic"}
        )

@app.post("/tarefas")
def adicionar_tarefa(tarefa: Tarefa, credentials: HTTPBasicCredentials = Depends(autenticar_usuario)):
    nova_tarefa = {
        "nome": tarefa.nome,
        "descricao": tarefa.descricao,
        "concluida": False
    }
    tarefas.append(nova_tarefa)
    return {"mensagem": "Tarefa adicionada com sucesso", "tarefa": nova_tarefa}


@app.get("/tarefas")
def listar_tarefas(page: int = 1, limit: int = 10, credentials: HTTPBasicCredentials = Depends(autenticar_usuario)):
    return tarefas    
    if page <1 or limit <1:
        raise HTTPException(status_code=400, detail="Página ou limite não podem ter valores menores que 1")
    
    if not tarefas:
        return {"message":"Não existe nenhuma tarefa"}
    
start = (page - 1) * limit
end = start * limit


@app.put("/tarefas/{nome}")
def concluir_tarefa(nome: str, credentials: HTTPBasicCredentials = Depends(autenticar_usuario)):
    for tarefa in tarefas:
        if tarefa["nome"] == nome:
            tarefa["concluida"] = True
            return {"mensagem": "Tarefa marcada como concluída", "tarefa": tarefa}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")


@app.delete("/tarefas/{nome}")
def remover_tarefa(nome: str, credentials: HTTPBasicCredentials = Depends(autenticar_usuario)):
    for tarefa in tarefas:
        if tarefa["nome"] == nome:
            tarefas.remove(tarefa)
            return {"mensagem": "Tarefa removida com sucesso"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")