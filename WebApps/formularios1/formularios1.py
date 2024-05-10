from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def recibe_datos(): 
   nombre = request.form['nombre']
   contrasenya = request.form['contrasenya']
   return f'<h1>Nombre: {nombre}, Contraseña: {contrasenya}</h1>'

if __name__ == "__main__":
    app.run(debug=True)