from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return '¡Hola Mundo!'



@app.route("/blog/")
def lee_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    respuesta = requests.get(blog_url)
    todos_los_articulos = respuesta.json()
    #print(todos_los_articulos)
    return render_template("blog.html", articulos=todos_los_articulos)


if __name__ == "__main__":
    app.run(debug=True)


