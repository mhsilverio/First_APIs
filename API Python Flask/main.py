# python main.py
from flask import Flask, request, jsonify, json

app = Flask(__name__)

bd = [
    {"id": 1, "Nome": "Nome 1", "Email":"XXXXXXXXX@email.com", "Senha":"XXXXXXXXX"},
    {"id": 2, "Nome": "Nome 2", "Email":"XXXXXXXXX@email.com", "Senha":"XXXXXXXXX"},
    {"id": 3, "Nome": "Nome 3", "Email":"XXXXXXXXX@email.com", "Senha":"XXXXXXXXX"},
    {"id": 4, "Nome": "Nome 4", "Email":"XXXXXXXXX@email.com", "Senha":"XXXXXXXXX"},
    {"id": 5, "Nome": "Nome 5", "Email":"XXXXXXXXX@email.com", "Senha":"XXXXXXXXX"},
    ]

@app.route("/")
def ok():
    return "200 OK"

@app.route("/usuario", methods=["GET"])
def get():
    return jsonify(bd), 200

@app.route('/usuario/<int:id>', methods=["GET"])
def get_id(id):
    for usuario in bd:
        if(usuario["id"] == id):
            return jsonify(usuario), 200
    return jsonify({"Status": 404, "Mensagem": "Usuário não encontrado"})

@app.route('/usuario/<int:id>', methods=["PUT"])
def put(id):
    for usuario in bd:
        if(usuario["id"] == id):
            usuario["Email"] = request.get_json().get("Email")
            return jsonify(usuario), 200
    return jsonify({"Status": 404, "Mensagem": "Não encontrado"})

@app.route("/cadastrar", methods=["POST"])
def add():
    new = request.get_json()
    bd.append(new)
    return jsonify(new), 201

@app.route("/delete/<int:id>", methods=["DELETE"])
def delete(id):
    for usuario in bd:
       if(usuario["id"] == id):
           bd.remove(usuario)
           return jsonify(usuario), 201
    return{"Status": 404, "Mensagem": "Usuário não encontrado"}

# app.run(host = "0.0.0.0", port = 2000, debug = False)
if __name__ == '__main__':
    app.run(debug=True)