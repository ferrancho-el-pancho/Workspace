from flask import Flask, render_template
import random 
import datetime

app = Flask(__name__)


@app.route('/')
def home():
    numero_aleatorio = random.randint(1,10)
    anyo_actual = datetime.datetime.now().year
    return render_template("index.html", num=numero_aleatorio, anyo=anyo_actual)


if __name__ == "__main__":
    app.run(debug=True)


