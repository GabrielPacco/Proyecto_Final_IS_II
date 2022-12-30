from urllib import response
import requests
from flask import Flask, render_template, request, redirect, url_for, session, flash

from flask import Flask, session, redirect, g
from flask import request,flash
from flask import jsonify
from flask import render_template,url_for
from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from backend.blueprints.evento_blueprint import evento_blueprint
from backend.blueprints.ponente_blueprint import ponente_blueprint

from backend.models.evento import EventoModel
from backend.models.ponente import PonenteModel

app = Flask(__name__,template_folder='frontend/templates',static_folder='frontend/static')

app.secret_key= "averysecretkey"

#mysql = MySQL()
app.register_blueprint(evento_blueprint)
app.register_blueprint(ponente_blueprint)

cors = CORS(app)
#mysql = MySQL(app)
#mysql.init_app(app)

@app.route('/', methods=['GET','POST'])
def index():
    response = requests.post("http://127.0.0.1:5000/api/evento/get_all").json()
    return render_template('index.html', eventos=response)


@app.route('/home', methods=['GET','POST'])
def home():
    response = requests.post("http://127.0.0.1:5000/api/evento/get_all").json()
    print("respnjse",response)
    return render_template('home.html', eventos=response)
    
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/validate_login', methods = ['POST'])
def validate_login():
    if request.method == 'POST':
        correo = request.form['typeEmailX']
        password = request.form['typePasswordX']
        users=requests.post("http://127.0.0.1:5000/api/ponente/get_all").json()
        user={}
        for x in users:
            if x['correo']==correo:
                user=x
                break
        if not user:
            return "Not found"
        elif password == user['nombre']:
            session['correo'] = user['correo']
            return  redirect(url_for('home'))

    return redirect(url_for('error'))

@app.route('/error', methods=['GET'])
def error():
    return render_template('error.html')

@app.route('/logout')
def logout():
    if 'correo' in session:
        session.pop('correo', None)
        return render_template('index.html')

@app.route('/registro', methods=['GET'])
def Registro():
    return render_template('registrar.html')

@app.route('/evento/<int:id>', methods=['GET'])
def evento(id):
    query = {"id" : id}
    resp = requests.post("http://127.0.0.1:5000/api/evento/get", json=query).json()
    return render_template('evento.html', evento=resp)

@app.route('/create_evento', methods=['GET','POST'])
def create_evento():
    if request.method == 'POST':
        query= {
        'id_ponente' : 2,
        'nombre' : request.form['evento_nombre'],
        'detalles' : request.form['evento_detalles'],
        'link' : request.form['evento_link']}
        print(query)
        #print(nombre)
        resp = requests.post("http://127.0.0.1:5000/api/evento/create",json=query)
        print(resp)
        return  redirect('/')

    return render_template('create_evento.html')

@app.route('/profile/<int:id>', methods=['GET'])
def Profile(id):
    query = {"id" : id}
    resp = requests.post("http://127.0.0.1:5000/api/ponente/get", json=query).json()
    return render_template('profile.html', ponente=resp)

#branch diego

@app.route('/edit_evento/<int:id>', methods=['GET','POST'])
def Edit_evento(id):
    if request.method == 'POST':
        Query= {
        'id' : id,
        'id_ponente' : 2,
        'nombre' : request.form['evento_nombre'],
        'detalles' : request.form['evento_detalles'],
        'link' : request.form['evento_link']}
        requests.post("http://127.0.0.1:5000/api/evento/edit",json=Query)
        return  redirect('/home')

    return render_template('edit_evento.html')



if __name__ == "__main__":
    app.run(debug=True)
