from flask import Flask, render_template, jsonify
from logica_cafe import FabricaDeCafe

app = Flask(__name__)

# Esta es nuestra "Capa de Entrada" que recibe las peticiones
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pedir/<tipo>')
def pedir_cafe(tipo):
    # Usamos la fábrica para obtener el objeto
    mi_cafe = FabricaDeCafe.preparar_cafe(tipo)
    return jsonify({
        "mensaje": f"¡Tu {mi_cafe.nombre} está listo!",
        "ingredientes": mi_cafe.ingredientes
    })

if __name__ == '__main__':
    app.run(debug=True)