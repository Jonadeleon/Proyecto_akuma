from flask import Flask, render_template, request, redirect
# traemos dependecia de pymongo para la conexion a la base de datos
from pymongo import MongoClient

app = Flask(__name__)
# ponemos la conexion y la base de datos MUY IMPORTANTE TENER VERSION DE PYTHON ACTUALIZADO Y CONFIGURADO EN PYCHARM O NO FUNCIONARÁ EL ENLACE
client = MongoClient("mongodb+srv://karmaster:acm1ptcactm@cluster0-gsee8.mongodb.net/test?retryWrites=true&w=majority")
db = client["akuma"]
col = db["poderes_menores"]

@app.route('/')
def inicio():
    return render_template('index.html')

# Ruta para listar todas las clases, sólo acepta métodos GET y POST
# Usando GET obtenemos la lista de todas las clases, usando POST creamos una nueva
@app.route('/innatos', methods=['GET'])
def innatos():
    innatos = db.poderes_innatos.find().sort("name", 1)
    return render_template('innatos.html', innatos=innatos)

@app.route('/basicos', methods=['GET'])
def basicos():
    basicos = db.poderes_básicos.find().sort("name", 1)
    return render_template('basicos.html', basicos=basicos)

@app.route('/menores', methods=['GET'])
def menores():
    menores = db.poderes_menores.find().sort("name", 1)
    return render_template('menores.html', menores=menores)


@app.route('/mayores', methods=['GET'])
def mayores():
    mayores = db.poderes_mayores.find().sort("name", 1)
    return render_template('mayores.html', mayores=mayores)

@app.route('/superiores', methods=['GET'])
def superiores():
    superiores = db.poderes_superiores.find().sort("name", 1)
    return render_template('superiores.html', superiores=superiores)



if __name__ == "__main__":
    app.run(debug=True)