from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class Animal(BaseModel):
    id: int = random.randint()
    nome: str
    idade: int
    sexo: bool
    cor: str

@app.post("/animais")
def cadastrar_animais(animal: Animal):
    return {
        "nome": animal.nome,
        "idade": animal.idade,
        "sexo": animal.sexo,
        "cor": animal.cor
    }

@app.get("/animais")
def retornar_todos_animais():
    return 