from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hola_mundo():
    return '¡Hola, Mundo!'

@app.route('/adios')
def di_adios():
    return 'Adiós'

if __name__ == '__main__':
    app.run()