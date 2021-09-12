# uvicorn main:app --reload

import docker

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from starlette.requests import Request
from starlette.routing import request_response

app = FastAPI()

@app.get('/')
def ok():
    return "200 OK"

class Usuario(BaseModel):
    id: int
    Nome: str
    Email: str
    Senha: str

bd = [
    Usuario(id=1, Nome= "Nome 1", Email="XXXXXXXXX@email.com", Senha="XXXXXXXXX"),
    Usuario(id=2, Nome= "Nome 2", Email="XXXXXXXXX@email.com", Senha="XXXXXXXXX"),
    Usuario(id=3, Nome= "Nome 3", Email="XXXXXXXXX@email.com", Senha="XXXXXXXXX"),
    Usuario(id=4, Nome= "Nome 4", Email="XXXXXXXXX@email.com", Senha="XXXXXXXXX"),
    Usuario(id=5, Nome= "Nome 5", Email="XXXXXXXXX@email.com", Senha="XXXXXXXXX"),
    ]

@app.get("/usuarios")
def get():
    return bd

@app.get("/usuarios/{id_usuario}")
def get_id(id_usuario: int):
    for usuario in bd:
        if(usuario.id == id_usuario):
            return usuario
    return{"Status": 404, "Mensagem": "Usuário não encontrado"}

@app.post("/usuarios")
def add(usuario: Usuario):
    bd.append(usuario)
    return usuario

@app.put('/usuarios/{id_usuario}')
def put(id_usuario: int):
    for usuario in bd:
        if(usuario.id == id_usuario):
            usuario.Email = print(request_response("Email"))
            return usuario
    return {"Status": 404, "Mensagem": "Não encontrado"}

@app.delete("/usuarios/{id_usuario}")
def get_id(id_usuario: int):
    for usuario in bd:
        if(usuario.id == id_usuario):
           bd.remove(usuario)
           return usuario
    return{"Status": 404, "Mensagem": "Usuário não encontrado"}