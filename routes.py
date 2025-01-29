from app import app
from flask import render_template, request, flash, jsonify
import json
import os

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/loja")
def loja():
    return "Hello, loja"

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/cadastrarUsuario", methods=["GET", "POST"])
def cadastrarUsuario():
    if request.method == "POST":
        nome = request.form.get("nome")
        senha = request.form.get("senha")

        if not nome or not senha:
            return jsonify({"erro": "Nome e senha são obrigatórios!"}), 400

        # Verifica se o arquivo existe, se não, cria uma lista vazia
        if os.path.exists("usuarios.json"):
            with open("usuarios.json", "r", encoding="utf-8") as usuariosTemp:
                try:
                    usuarios = json.load(usuariosTemp)
                except json.JSONDecodeError:
                    usuarios = []  # Caso o JSON esteja vazio ou inválido
        else:
            usuarios = []

        # Verifica se o usuário já existe
        for usuario in usuarios:
            if usuario["nome"] == nome:
                flash ("erro: Usuário já cadastrado! Escolha outro nome.")
                return render_template ("cadastro.html")

        # Adiciona o novo usuário
        usuarios.append({"nome": nome, "senha": senha})

        # Salva no arquivo JSON
        with open("usuarios.json", "w", encoding="utf-8") as gravarTemp:
            json.dump(usuarios, gravarTemp, indent=4, ensure_ascii=False)

        return render_template ("login.html")

    return render_template("login.html")



@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        nome = request.form.get("nome")
        senha = request.form.get("senha")


        with open ("usuarios.json") as usuariosTemp:
            usuarios = json.load(usuariosTemp)
            cont = 0
            for usuario in usuarios:
                cont += 1
                if usuario["nome"] == nome and usuario["senha"] == senha:
                    return render_template("index.html")
                
                if cont >= len(usuarios):
                    flash("Usuário ou senha incorretos")
                    return render_template("login.html")

    return render_template("login.html")        

