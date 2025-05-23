from app import app
from flask import render_template, request, flash, jsonify, redirect, url_for, session # Importando as classes

import json
import os
import ast

logado = False

class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def autenticar(self, nome, senha):
        return self.nome == nome and self.senha == senha

class Administrador(Usuario):
    def __init__(self, nome="adm", senha="000"):
        super().__init__(nome, senha)

    def autenticar(self, nome, senha):
        if super().autenticar(nome, senha):
            return "administrador"
        return None

def carregar_usuarios():
    with open("usuarios.json") as usuariosTemp:
        usuarios_data = json.load(usuariosTemp) #A função carrega os dados do JSON e cria objetos da classe Usuario
    return [Usuario(u["nome"], u["senha"]) for u in usuarios_data] #retornando uma lista desses objetos.


class Pessoa:
    def __init__(self, nome, senha):
        self.__nome = nome
        self.__senha = senha
    
    def get_nome(self):
        return self.__nome
    
    def get_senha(self):
        return self.__senha

    def to_dict(self): # Retorna o usuário como dicionário para ser salvo no JSON
        return {"nome": self.__nome, "senha": self.__senha}
    
class GerenciadorUsuarios:
    ARQUIVO_JSON = "usuarios.json" #Define o nome do arquivo onde os usuários serão armazenados.

    @staticmethod
    def carregar_usuarios(): #Carrega os usuários do JSON, retorna lista vazia se o arquivo não existir ou estiver inválido.
        if os.path.exists(GerenciadorUsuarios.ARQUIVO_JSON): #Verifica se o arquivo JSON existe
            try:
                with open(GerenciadorUsuarios.ARQUIVO_JSON, "r", encoding="utf-8") as file: #tenta abrir e carregar os dados.
                    return json.load(file)
            except json.JSONDecodeError:
                return []  # Retorna lista vazia se o JSON estiver corrompido
        return []

    @staticmethod
    def salvar_usuario(usuario): #Adiciona um novo usuário e salva no JSON
        usuarios = GerenciadorUsuarios.carregar_usuarios()

        # Verifica se o usuário já existe
        for u in usuarios:
            if u["nome"] == usuario.get_nome():
                return False  # Usuário já cadastrado (duplicação)

        # Adiciona novo usuário e salva
        usuarios.append(usuario.to_dict())
        with open(GerenciadorUsuarios.ARQUIVO_JSON, "w", encoding="utf-8") as file:
            json.dump(usuarios, file, indent=4, ensure_ascii=False)
        
        return True  # Cadastro bem-sucedido


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/loja")
def loja():
    return "Hello, loja"

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/troca_devolucao")
def troca_devolucao():
    return render_template ("troca_devolucao.html")


@app.route("/compra")
def compra():
    return render_template("compra.html")

@app.route("/compra2")
def compra2():
    return render_template("compra2.html")

@app.route("/compra3")
def compra3():
    return render_template("compra3.html")

@app.route("/compra4")
def compra4():
    return render_template("compra4.html")

@app.route("/compra5")
def compra5():
    return render_template("compra5.html")

@app.route("/compra6")
def compra6():
    return render_template("compra6.html")

@app.route("/compra7")
def compra7():
    return render_template("compra7.html")

@app.route("/compra8")
def compra8():
    return render_template("compra8.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/adm")
def adm():
    if logado == True:
        with open ("usuarios.json") as usuariosTemp:
            usuarios = json.load(usuariosTemp)
        return render_template ("administrador.html",usuarios=usuarios) #Passa a variável usuarios para ser usada na página.
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
    nome = request.form.get("nome")
    senha = request.form.get("senha")

    if not nome or not senha:
        return jsonify({"erro": "Nome e senha são obrigatórios!"}), 400

    novo_usuario = Pessoa(nome, senha)

    if GerenciadorUsuarios.salvar_usuario(novo_usuario): #cadastrar usuário 
        flash("Usuário cadastrado com sucesso!", "success")
        return redirect(url_for('login'))
    else:
        flash("Usuário já cadastrado! Escolha outro nome.", "danger")
        return redirect(url_for('cadastro'))



@app.route("/login", methods=["GET", "POST"])
def login():
    global logado
    logado = False

    if request.method == 'POST':
        nome = request.form.get("nome")
        senha = request.form.get("senha")

        admin = Administrador()
        if admin.autenticar(nome, senha) == "administrador":
            logado = True
            return render_template("administrador.html")

        usuarios = carregar_usuarios()
        for usuario in usuarios:
            if usuario.autenticar(nome, senha):
                session["nome"] = usuario.nome
                return render_template("index.html", nome=session["nome"])

        # Se chegar aqui, o usuário errou
        flash("Usuário ou senha incorretos", "danger")
        return redirect(url_for('login'))  # Redireciona para evitar o flash ao carregar a página

    return render_template("login.html")

@app.route("/excluirUsuario", methods=["POST"])
def excluirUsuario():
    global logado
    logado = True
    usuario = request.form.get("usuarioPexcluir") #Pega o usuário a ser excluído a partir do formulário
    usuarioDict = ast.literal_eval(usuario) #converte a string em um dicionário Python.
    nome = usuarioDict["nome"] #Extrai o nome do usuário que será excluído.
    with open ("usuarios.json") as usuariosTemp:
        usuariosJson = json.load(usuariosTemp)
        for c in usuariosJson:
            if c == usuarioDict:
                usuariosJson.remove(usuarioDict) #remove da lista caso responda a usuarioDict
                with open("usuarios.json", "w") as usuariosAexcluir:  
                    json.dump(usuariosJson, usuariosAexcluir, indent=4) #Salva a lista atualizada de usuários
    flash(F"{nome} EXCLUÍDO(A)", "success")
    return render_template("administrador.html")
