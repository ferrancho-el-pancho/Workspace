from flask import Flask, render_template, request
import random

app = Flask(__name__)


aleatorio = random.randint(0,9)


@app.route('/')
def hola_mundo():
    return render_template('index.html')
    

@app.route('/<int:acierto>')
def comparar_numero(acierto):
    if acierto > aleatorio:
        return render_template('alto.html')
    elif acierto < aleatorio:
        return render_template('bajo.html')
    else: 
        return render_template('acertaste.html')


if __name__ == '__main__':
    app.run(debug=True)