from flask import Flask, render_template, request
import random

app = Flask(__name__)


aleatorio = random.randrange(0,9)


@app.route('/')
def hola_mundo():
    return '<h1> Acierta un número entre el 0 y el 9 <h1>' '<iframe src = "https://giphy.com/embed/Dg4TxjYikCpiGd7tYs" width="480" height="480">'

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