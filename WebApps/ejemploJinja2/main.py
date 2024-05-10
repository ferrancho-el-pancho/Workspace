from flask import Flask, render_template
import random 
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return '¡Hola Mundo!'

@app.route('/acierta/<nombre>')
def acierta(nombre):
    url_sexo =f"https://api.genderize.io?name={nombre}"
    respuesta_sexo=requests.get(url_sexo)
    datos_sexo=respuesta_sexo.json()
    sexo = datos_sexo["gender"]
    if sexo == 'male':
        sexo ='hombre'
    else:
        sexo = 'mujer'

    url_edad = f'https://api.agify.io/?name={nombre}'
    respuesta_edad = requests.get(url_edad)
    datos_edad = respuesta_edad.json()
    edad = datos_edad ['age']
    return render_template('acierta.html',sexo=sexo, nombre_persona=nombre, edad=edad)


    


if __name__ == "__main__":
    app.run(debug=True)


