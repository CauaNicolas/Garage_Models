from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'PROJETINHO'

from routes import*

if __name__ == "__main__":
    app.run(debug=True)
    
# Seu catálogo de miniaturas...
MINIATURAS_BD = [
    {"id": 1, "nome": "Nissan Skyline GT-R R34 2000", "imagem": "Nissan Skyline GT-R R34 2000.png", "tipo": "carro", "preco": 99.90},
    {"id": 2, "nome": "BMW M5 F90 2022", "imagem": "BMW M5 F90 2022.png", "tipo": "carro", "preco": 109.90},
    {"id": 3, "nome": "Honda Acura NSX 2018", "imagem": "Honda Acura NSX 2018.png", "tipo": "carro", "preco": 99.90},
    {"id": 4, "nome": "Porsche 911 GT3 RS 2023", "imagem": "Porsche 911 GT3 RS 2023.png", "tipo": "carro", "preco": 149.90},
    {"id": 5, "nome": "Honda Type R 2023", "imagem": "Honda Type R 2023.png", "tipo": "carro", "preco": 79.90},
    {"id": 6, "nome": "BMW R1250 GS 2022", "imagem": "Moto BMW R1250 GS 2022.png", "tipo": "moto", "preco": 79.90},
    {"id": 7, "nome": "Honda CBR1000RR-R 2022", "imagem": "Moto Honda CBR1000RR-R 2022.png", "tipo": "moto", "preco": 69.90},
    {"id": 8, "nome": "Honda Hornet 2012", "imagem": "Moto Honda Hornet 2012.png", "tipo": "moto", "preco": 89.90},
    {"id": 9, "nome": "Yamaha YZF R1 2013", "imagem": "Moto Yamaha YZF R1 2013.png", "tipo": "moto", "preco": 149.90},
    {"id": 10, "nome": "Renault Kwid 2019", "imagem": "Renault Kwid 2019.png", "tipo": "carro", "preco": 59.90},
    {"id": 11, "nome": "Volkswagen Passat 2017", "imagem": "Volkswagen Passat 2017.png", "tipo": "carro", "preco": 89.90},
    {"id": 12, "nome": "Honda CR-V 2020", "imagem": "Honda CR-V 2020.png", "tipo": "carro", "preco": 99.90},
    {"id": 13, "nome": "Toyota Corolla 2019", "imagem": "Toyota Corolla 2019.png", "tipo": "carro", "preco": 79.90},
    {"id": 14, "nome": "Ford Mustang 2020", "imagem": "Ford Mustang 2020.png", "tipo": "carro", "preco": 149.90},
    {"id": 15, "nome": "Hyundai Elantra 2017", "imagem": "Hyundai Elantra 2017.png", "tipo": "carro", "preco": 69.90},
    {"id": 16, "nome": "Jaguar XF S-Type 2018", "imagem": "Jaguar XF S-Type 2018.png", "tipo": "carro", "preco": 149.90},
    {"id": 17, "nome": "Audi A1 Sportback 2018", "imagem": "Audi A1 Sportback 2018.png", "tipo": "carro", "preco": 89.90},
    {"id": 18, "nome": "Audi A4 2018", "imagem": "Audi A4 2018.png", "tipo": "carro", "preco": 109.90},
    {"id": 19, "nome": "Audi TT RS 2018", "imagem": "Audi TT RS 2018.png", "tipo": "carro", "preco": 109.90},
    {"id": 20, "nome": "Mercedes-Benz ML 250 2015", "imagem": "Mercedes-Benz ML 250 2015.png", "tipo": "carro", "preco": 89.90},
    {"id": 21, "nome": "Mercedes-Benz Classe C 2019", "imagem": "Mercedes-Benz Classe C 2019.png", "tipo": "carro", "preco": 109.90},
    {"id": 22, "nome": "Mercedes G63 2021", "imagem": "Mercedes G63 2021.png", "tipo": "carro", "preco": 149.90},
    {"id": 23, "nome": "Yamaha MT-10 2017", "imagem": "Yamaha MT-10 2017.png", "tipo": "moto", "preco": 149.90},
    {"id": 24, "nome": "Honda CBR600RR 2019", "imagem": "Honda CBR600RR 2019.png", "tipo": "moto", "preco": 109.90},
    {"id": 25, "nome": "Honda VFR800 2015", "imagem": "Honda VFR800 2015.png", "tipo": "moto", "preco": 89.90},
    {"id": 26, "nome": "Kawasaki Ninja 300 2016", "imagem": "Kawasaki Ninja 300 2016.png", "tipo": "moto", "preco": 79.90},
    {"id": 27, "nome": "Yamaha FZ MT-09 2023", "imagem": "Yamaha FZ MT-09 2023.png", "tipo": "moto", "preco": 109.90},
]