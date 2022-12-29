@app.route('/', methods=['GET','POST'])
def index():
    print("entre")
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
def registro():
    return render_template('registrar.html')

@app.route('/evento/<int:id>', methods=['GET'])
def evento(id):
    query = {"id" : id}
    resp = requests.post("http://127.0.0.1:5000/api/evento/get", json=query).json()
    return render_template('evento.html', evento=resp)

@app.route('/create_evento', methods=['GET','POST'])
def create_evento():
    if request.method == 'POST':
        query= {'id_ponente' : 2,
        'nombre' : request.form['evento_nombre'],
        'detalles' : request.form['evento_detalles'],
        'link' : request.form['evento_link']}
        print(query)
        #print(nombre)
        resp = requests.post("http://127.0.0.1:5000/api/evento/create",json=query)
        print(resp)
        return  redirect('/home')

    return render_template('create_evento.html')

@app.route('/profile/<int:id>', methods=['GET'])
def profile(id):
    query = {"id" : id}
    resp = requests.post("http://127.0.0.1:5000/api/ponente/get", json=query).json()
    return render_template('profile.html', ponente=resp)

if __name__ == "__main__":
    app.run(debug=True)