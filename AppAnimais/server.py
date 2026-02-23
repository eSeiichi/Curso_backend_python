from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4, UUID

app = FastAPI()

class Animal(BaseModel):
    id: Optional[UUID] = None
    nome: str
    idade: int
    sexo: str
    cor: str

banco: List[Animal] = []


@app.get("/animais")
def listar_animais():
    return banco


@app.post("/animais")
def criar_animal(animal: Animal):
    animal.id = uuid4()
    banco.append(animal)
    return None

@app.get("/animais/{id}")
def achar_animal(id):
    for char in banco:
        if banco[char][0] == id:
            return banco[char]