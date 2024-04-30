from flask import Flask, render_template, request

app = Flask(__name__)

def pon_negrita(function):
    def envoltorio():
        return '<b>' + function() + '</b>'
    return envoltorio

def pon_enfasis(function):
    def envoltorio():
        return '<em>' + function() + '</em>'
    return envoltorio
    
def pon_subrayado(function):
    def envoltorio():
        return '<u>' + function() + '</u>'
    return envoltorio


@app.route('/')
def hola_mundo():
    return '<h1> ¡Hola, Mundo! <h1>'


@app.route('/adios')
@pon_negrita
@pon_enfasis
@pon_subrayado
def di_adios():
    return 'Adiós'

@app.route ('/nombreusuario/<nombreusuario>')
def saludo (nombreusuario):
    return f'Hola querido {nombreusuario}!'

if __name__ == '__main__':
    app.run(debug=True)