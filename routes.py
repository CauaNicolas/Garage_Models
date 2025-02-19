from app import app
from flask import render_template, request, flash, jsonify, redirect
import json
import os
import ast

logado = False

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/loja")
def loja():
    return "Hello, loja"

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/adm")
def adm():
    if logado == True:
        with open ("usuarios.json") as usuariosTemp:
            usuarios = json.load(usuariosTemp)
        return render_template ("administrador.html",usuarios=usuarios)
    if logado == False:
        return render_template ("login.html")
    
    return render_template("administrador.html")

@app.route("/administrador", methods=["GET", "POST"])
def administrador():
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
                flash ("Usuário já cadastrado! Escolha outro nome.", "danger")
                return render_template ("administrador.html")

        # Adiciona o novo usuário
        usuarios.append({"nome": nome, "senha": senha})

        # Salva no arquivo JSON
        with open("usuarios.json", "w", encoding="utf-8") as gravarTemp:
            json.dump(usuarios, gravarTemp, indent=4, ensure_ascii=False)

        flash ("Usuário cadastrado com sucesso!", "success")
        return render_template ("administrador.html")
    
    return redirect("/adm")

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
                flash ("Usuário já cadastrado! Escolha outro nome.", "danger")
                return render_template ("cadastro.html")

        # Adiciona o novo usuário
        usuarios.append({"nome": nome, "senha": senha})

        # Salva no arquivo JSON
        with open("usuarios.json", "w", encoding="utf-8") as gravarTemp:
            json.dump(usuarios, gravarTemp, indent=4, ensure_ascii=False)

        flash ("Usuário cadastrado com sucesso!", "success")
        return render_template ("login.html")

    return render_template("login.html")



@app.route("/login", methods=["GET", "POST"])
def login():


    global logado
    logado = False

    if request.method == "POST":
        nome = request.form.get("nome")
        senha = request.form.get("senha")


        with open ("usuarios.json") as usuariosTemp:
            usuarios = json.load(usuariosTemp)
            cont = 0
            for usuario in usuarios:
                cont += 1

                if nome == "adm" and senha == "000":
                    logado = True
                    return render_template("administrador.html")

                if usuario["nome"] == nome and usuario["senha"] == senha:
                    return render_template("index.html")
                
                if cont >= len(usuarios):
                    flash("Usuário ou senha incorretos", "danger")
                    return render_template("login.html")

    return render_template("login.html")        

@app.route("/excluirUsuario", methods=["POST"])
def excluirUsuario():
    global logado
    logado = True
    usuario = request.form.get("usuarioPexcluir")
    usuarioDict = ast.literal_eval(usuario)
    nome = usuarioDict["nome"]
    with open ("usuarios.json") as usuariosTemp:
        usuariosJson = json.load(usuariosTemp)
        for c in usuariosJson:
            if c == usuarioDict:
                usuariosJson.remove(usuarioDict)
                with open("usuarios.json", "w") as usuariosAexcluir:
                    json.dump(usuariosJson, usuariosAexcluir, indent=4)
    flash(F"{nome} EXCLUÍDO(A)", "success")
    return render_template("administrador.html")
