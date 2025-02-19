import json
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
        usuarios_data = json.load(usuariosTemp)
    return [Usuario(u["nome"], u["senha"]) for u in usuarios_data]