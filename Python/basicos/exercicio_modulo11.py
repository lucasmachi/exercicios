from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

#validação automatica usando pydantic

app = FastAPI()

tarefas = []


class Tarefa(BaseModel):
    nome: str
    descricao: str
    concluida: bool = False


@app.post("/tarefas")
def adicionar_tarefa(tarefa: Tarefa):
    tarefas.append(tarefa)
    return {"mensagem": "Tarefa adicionada com sucesso", "tarefa": tarefa}


@app.get("/tarefas")
def listar_tarefas():
    return tarefas


@app.put("/tarefas/{nome}")
def concluir_tarefa(nome: str):
    for tarefa in tarefas:
        if tarefa.nome == nome:
            tarefa.concluida = True
            return {"mensagem": "Tarefa marcada como concluída", "tarefa": tarefa}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")


@app.delete("/tarefas/{nome}")
def remover_tarefa(nome: str):
    for tarefa in tarefas:
        if tarefa.nome == nome:
            tarefas.remove(tarefa)
            return {"mensagem": "Tarefa removida com sucesso"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")