from flask import Flask, render_template, request, redirect
# traemos dependecia de pymongo para la conexion a la base de datos
from pymongo import MongoClient

app = Flask(__name__)
# ponemos la conexion y la base de datos MUY IMPORTANTE TENER VERSION DE PYTHON ACTUALIZADO Y CONFIGURADO EN PYCHARM O NO FUNCIONARÁ EL ENLACE
client = MongoClient("mongodb+srv://karmaster:acm1ptcactm@cluster0-gsee8.mongodb.net/test?retryWrites=true&w=majority")
db = client.akuma

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

@app.route('/subida')
def subida():
    name = request.args['name']
    description = request.args['descripcion']
    stat_bonus = request.args['stat_bonus']
    dice_pv = request.args['dados_pv']
    dice_pm = request.args['dados_pm']
    licencias = request.args['licencias']
    hab1 = request.args['hab1']

    db.clases.insert_one(
        {
            "name": name,
            "descripcion": description,
            "stat_bonus": stat_bonus,
            "dice_pv": dice_pv,
            "dice_pm": dice_pm,
            "licencias": licencias,
            "hab1": hab1
        }
    )
    return redirect('/clases')


if __name__ == "__main__":
    app.run(debug=True)