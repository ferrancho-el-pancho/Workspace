from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class FormularioCafe(FlaskForm):
    cafe = StringField('Nombre del café', validators=[DataRequired()])
    submit = SubmitField('Envía')

# Ejercicio:
# Añade los campos: URL ubicación, hora apertura, hora cierree, valoración café, valoración wifi, valoración enchufe corriente
# Haz que los campos café/wifi/corriente sea un elemento de selección de 0 a 5.
# p.ej. Puedes usar emojis ☕️/💪/✘/🔌
# Haz que todos los campos sean requeridos excepto submit
# Usa un validador para que el campo URL tenga una URL introducida.
# ---------------------------------------------------------------------------


# Todas las rutas Flask debajo
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/anyade')
def anyade_cafe():
    formulario = FormularioCafe()
    if formulario.validate_on_submit():
        print("OK")
    # Ejercicio:
    # Haz que el formulario escriba una nueva fila en datos-cafes.csv
    # con   if formulario.validate_on_submit()
    return render_template('anyade.html', form=formulario)


@app.route('/cafes')
def cafes():
    with open('datos-cafes.csv', newline='') as fichero_csv:
        datos_csv = csv.reader(fichero_csv, delimiter=',')
        lista_de_filas = []
        for row in datos_csv:
            lista_de_filas.append(row)
    return render_template('cafes.html', cafes=lista_de_filas)


if __name__ == '__main__':
    app.run(debug=True)
