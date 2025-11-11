from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/saludo",methods=["POST"])
def saludo():
    nombre = request.form.get("nombre")
    return f"Hola {nombre} bienvenido a Flask."

if __name__ == "__main__":
    app.run(debug=True)