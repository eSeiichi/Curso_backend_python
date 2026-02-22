from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Bem-vindo à API de produtos!"}


class Produto(BaseModel): # Define a classe Produto que herda de BaseModel
    nome: str
    preco: float
    


@app.post("/produtos")
def produtos(produto: Produto):
    return {"message": f"Produto ({produto.nome} - R$ {produto.preco}) cadastrado com sucesso!"}

