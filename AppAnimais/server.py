from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4, UUID

app = FastAPI()

class Animal(BaseModel):
    id: Optional[str] = None
    nome: str
    idade: int
    sexo: str
    cor: str

banco: List[Animal] = []


@app.get("/animais")
def listar_animais():
    return banco


@app.get("/animais/{id_animal}")
def obter_animal(id_animal: str):
    for animal in banco:
        if animal.id == id_animal:
            return animal
    return {"erro": "animal não localizado"}

@app.delete("/animais/{id_animal}")
def deletar_animal(id_animal: str):
    posicao = -1
    # buscar o index do animal
    for index, animal in enumerate(banco):
        if animal.id == id_animal:
            posicao = index
            break
    if posicao != -1:
        banco.pop(posicao)
        return {"mesage": "animal removido com sucesso!"}
    else:
        return{"erro": "Animal não localizado"}

@app.post("/animais")
def criar_animal(animal: Animal):
    animal.id = str(uuid4())
    banco.append(animal)
    return None