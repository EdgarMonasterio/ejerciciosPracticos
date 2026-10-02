from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def inicio():
    return jsonify({
        "mensaje": "API funcionando",
        "curso": "Desarrollo de APIs"
    })


@app.route("/alumnos")
def alumnos():
    return jsonify([
        {
            "id": 1,
            "nombre": "Ana"
        },
        {
            "id": 2,
            "nombre": "Carlos"
        }
    ])


@app.route("/redes")
def redes():
    return jsonify({
        "mensaje": "Hola desde de Redes"
    })


if __name__ == "__main__":
    app.run(debug=True)