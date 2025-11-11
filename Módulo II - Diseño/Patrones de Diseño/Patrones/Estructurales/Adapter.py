""" 
Ejemplo:
Imagina que tu app espera “leer_texto()”, pero una librería externa solo ofrece “get_bytes()” en binario; el adaptador convierte bytes a texto.

"""

# Interfaz que el cliente espera
class LectorTexto:
    def leer_texto(self) -> str:
        raise NotImplementedError

# Servicio existente (incompatible)
class LectorBinario:
    def get_bytes(self) -> bytes:
        return b"Hola desde binario"

# Adaptador: traduce de bytes a str
class AdaptadorBinarioATexto(LectorTexto):
    def __init__(self, servicio: LectorBinario):
        self.servicio = servicio

    def leer_texto(self) -> str:
        datos = self.servicio.get_bytes()      # llama a la interfaz existente
        return datos.decode("utf-8")           # adapta el formato

# Uso por parte del "cliente"
def mostrar(lector: LectorTexto):
    print(lector.leer_texto())

mostrar(AdaptadorBinarioATexto(LectorBinario()))
