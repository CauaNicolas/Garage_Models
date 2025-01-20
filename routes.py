from app import app
from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/loja")
def loja():
    return "Hello, loja"

@app.route("/login")
def login():
    return "Hello, login"