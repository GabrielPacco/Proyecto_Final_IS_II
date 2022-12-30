from urllib import response
import requests

from flask import Flask, session, redirect, g
from flask import request
from flask import jsonify
from flask import render_template,url_for
from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from backend.blueprints.evento_blueprint import evento_blueprint
#from backend.blueprints.ponente_blueprint import ponente_blueprint
#from backend.blueprints.asistente_blueprint import asistente_blueprint
from backend.infrastructure.asistente_repository import AsistenteRepository

app = Flask(__name__,template_folder='frontend/templates',static_folder='frontend/static')

app.secret_key= "averysecretkey"



app.register_blueprint(evento_blueprint)
#app.register_blueprint(ponente_blueprint)
#app.register_blueprint(asistente_blueprint)

cors = CORS(app)

#comments
@app.route('/', methods=['GET'])
def index():
    response = requests.post("http://127.0.0.1:5000/api/evento/get_all").json()
    return render_template('home.html', eventos=response)

 
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        
        correo = request.form['typeEmailX']
        password = request.form['typePasswordX']
        # curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # curl.execute("SELECT * FROM usuario WHERE =%s",[correo])
        # user = curl.fetchone()
        users=requests.post("http://127.0.0.1:5000/api/ponente/get_all")
        print(users)
        user={}

        for x in users:
            if x['correo']==correo:
                user=x
                break
        
            

        # curl.close()
        if not user:
            return "Not found"
        elif password == user['nombre']:
            session['correo'] = user['correo']
            return  redirect(url_for('index'))
        else:
            return redirect(url_for('Registro'))

    return render_template('login.html')

@app.route('/registro', methods=['GET','POST'])
def registro():
    if request.method == 'POST':
        nombres = request.form['nombre']
        apellidos = request.form['apellidos']
        email = request.form['email']
        asistente = AsistenteRepository()
        asistente.create(nombres,apellidos,email)
        return render_template('home.html')
    return render_template('registrar.html')

@app.route('/evento/<int:id>', methods=['GET'])
def evento(id):
    query = {"id" : id}
    resp = requests.post("http://127.0.0.1:5000/api/evento/get", json=query).json()
    return render_template('evento.html', evento=resp)

@app.route('/profile/<int:id>', methods=['GET'])
def profile(id):
    query = {"id" : id}
    resp = requests.post("http://127.0.0.1:5000/api/ponente/get", json=query).json()
    return render_template('profile.html', ponente=resp)

if __name__ == "__main__":
    app.run(debug=True)

#branch: gabriel