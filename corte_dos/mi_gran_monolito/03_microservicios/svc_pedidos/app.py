from flask import Flask, jsonify, request
import requests # El "teléfono" para llamar al otro servicio

app = Flask(__name__)
db_pedidos = []

@app.route('/pedir', methods=['POST'])
def crear():
    data = request.json
    id_prod = data.get("id")

    # PATRÓN PROXY: Llamada remota en lugar de llamada local
    try:
        # Intentamos contactar al servicio de productos en el puerto 5000
        respuesta = requests.get(f"http://127.0.0.1:5000/productos/{id_prod}")
        
        if respuesta.status_code == 200:
            nuevo = {"id": len(db_pedidos) + 1, "prod_id": id_prod}
            db_pedidos.append(nuevo)
            return jsonify({"msg": "Pedido creado con éxito", "detalle": nuevo}), 201
        else:
            return jsonify({"msg": "Error: El producto no existe en el catálogo"}), 404

    except requests.exceptions.ConnectionError:
        return jsonify({"msg": "Error crítico: El servicio de Productos está caído"}), 503

if __name__ == '__main__':
    app.run(port=5001) # OTRO PUERTO