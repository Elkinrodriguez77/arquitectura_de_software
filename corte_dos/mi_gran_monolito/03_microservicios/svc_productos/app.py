from flask import Flask, jsonify

app = Flask(__name__)

# Base de datos aislada
db_productos = {
    1: {"nombre": "Laptop", "precio": 1000},
    2: {"nombre": "Mouse", "precio": 20}
}

@app.route('/productos', methods=['GET'])
def listar():
    return jsonify(db_productos)

# Ruta para verificar si un producto existe (para que otros servicios la usen)
@app.route('/productos/<int:id_prod>', methods=['GET'])
def verificar(id_prod):
    if id_prod in db_productos:
        return jsonify(db_productos[id_prod]), 200
    return jsonify({"error": "No encontrado"}), 404

if __name__ == '__main__':
    app.run(port=5000) # SU PROPIO PUERTO