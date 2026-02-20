from fastapi import FastAPI

app = FastAPI()

@app.get("/ola/{nome}") #parâmetro path
async def home(nome:str): #bom cololcar essa tipagem, para facilitar o debbug e na inserção de dados
    texto = f"olá {nome}"
    return {"mensage": texto}

@app.get("/quadrado/{num}")
def quadrado(num:int):
    ress = num*num
    texto = f"o quadrado de {num} é {ress}"
    return texto
    
@app.get("/dobro") #parametro query
def dobro(num:int):
    ress = num *2
    return {"resultado": f"O dobro de {num} é {ress}"}

# criando uma função para cada verbo http na mesma rota (profile)
'''
@app.get("/profile")
async def profile():
    return{"name": "claudio pipi"}


@app.post("/profile")
async def signup():
    return{"message": "Perfil criado com sucesso!"}


@app.put("/profile")
async def update():
    return{"message": "Perfil atualizado com sucesso!"}

@app.delete("/profile")
async def remover():
    return{"message": "Perfil deletado com sucesso!"}
'''