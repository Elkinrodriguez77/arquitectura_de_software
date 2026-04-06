from flask import Flask, jsonify, request
from productos import ModuloProductos
from pedidos import ModuloPedidos

app = Flask(__name__)

# Instanciamos los módulos (Simulamos servicios)
servicio_productos = ModuloProductos()
servicio_pedidos = ModuloPedidos()

@app.route('/productos', methods=['GET'])
def listar():
    return jsonify(servicio_productos.obtener_todo())

@app.route('/pedir', methods=['POST'])
def pedir():
    data = request.json
    # Pasamos el servicio de productos como dependencia
    exito, detalle = servicio_pedidos.crear(data.get("id"), servicio_productos)
    
    if exito:
        return jsonify({"msg": "OK", "detalle": detalle}), 201
    return jsonify({"msg": "Producto no encontrado"}), 404

if __name__ == '__main__':
    app.run(port=5000)