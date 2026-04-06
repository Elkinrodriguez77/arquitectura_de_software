
from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulación de Base de Datos Única (Acoplamiento de datos)
db_productos = {
    1: {"nombre": "Laptop", "precio": 1000, "stock": 5},
    2: {"nombre": "Mouse", "precio": 20, "stock": 10}
}
db_pedidos = []

@app.route('/productos', methods=['GET'])
def listar_productos():
    return jsonify(db_productos)

@app.route('/pedir', methods=['POST'])
def crear_pedido():
    data = request.json
    id_prod = data.get("id")
    # Lógica de negocio mezclada
    if id_prod in db_productos and db_productos[id_prod]["stock"] > 0:
        db_productos[id_prod]["stock"] -= 1
        db_pedidos.append({"id_prod": id_prod, "estado": "completado"})
        return jsonify({"msg": "Pedido realizado"}), 201
    return jsonify({"msg": "Error de stock"}), 400

if __name__ == '__main__':
    app.run(port=5000)