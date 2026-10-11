from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'PROJETINHO'

from routes import*

if __name__ == "__main__":
    app.run(debug=True)
    
# Seu catálogo de miniaturas...
MINIATURAS_BD = [
    {"id": 1, "nome": "Nissan Skyline GT-R R34 2000", "imagem": "Nissan Skyline GT-R R34 2000.png", "preco": 99.90},
    {"id": 2, "nome": "BMW M5 F90 2022", "imagem": "BMW M5 F90 2022.png", "preco": 109.90},
    {"id": 3, "nome": "Honda Acura NSX 2018", "imagem": "Honda Acura NSX 2018.png", "preco": 99.90},
    {"id": 4, "nome": "Porsche 911 GT3 RS 2023", "imagem": "Porsche 911 GT3 RS 2023.png", "preco": 149.90},
    {"id": 5, "nome": "Moto BMW R1250 GS 2022", "imagem": "Moto BMW R1250 GS 2022.png", "preco": 79.90},
    {"id": 6, "nome": "Moto Honda CBR1000RR-R 2022", "imagem": "Moto Honda CBR1000RR-R 2022.png", "preco": 69.90},
    {"id": 7, "nome": "Moto Honda Hornet 2012", "imagem": "Moto Honda Hornet 2012.png", "preco": 89.90},
    {"id": 8, "nome": "Moto Yamaha YZF R1 2013", "imagem": "Moto Yamaha YZF R1 2013.png", "preco": 149.90},
]