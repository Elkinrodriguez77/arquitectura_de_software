""" 
Ejemplo: 
Escenario: queremos leer y procesar texto; el componente base devuelve el texto, y decoradores opcionales añaden mayúsculas y recorte de espacios sin tocar la clase base.
"""

from abc import ABC, abstractmethod

# Interfaz del componente
class Lector(ABC):
    @abstractmethod
    def leer(self) -> str:
        pass

# Componente concreto
class LectorBase(Lector):
    def __init__(self, contenido: str):
        self._contenido = contenido
    def leer(self) -> str:
        return self._contenido

# Decorador base
class LectorDecorador(Lector):
    def __init__(self, envuelto: Lector):
        self._envuelto = envuelto
    def leer(self) -> str:
        # delega en el objeto envuelto
        return self._envuelto.leer()

# Decorador 1: recorta espacios
class RecortarEspacios(LectorDecorador):
    def leer(self) -> str:
        texto = super().leer()
        return texto.strip()

# Decorador 2: convierte a mayúsculas
class AMayusculas(LectorDecorador):
    def leer(self) -> str:
        texto = super().leer()
        return texto.upper()

# Uso: composición dinámica por apilamiento
if __name__ == "__main__":
    base = LectorBase("  hola mundo  ")
    limpio = RecortarEspacios(base)           # agrega recorte
    limpio_mayus = AMayusculas(limpio)        # agrega mayúsculas encima
    print(limpio_mayus.leer())                # -> "HOLA MUNDO"



"""
super() es una función incorporada de Python; no necesitas declararla tú, viene en el lenguaje y sirve para obtener un “proxy” hacia la clase base que corresponde según el orden de resolución de métodos (MRO) de la instancia actual.​

Qué hace exactamente
Cuando llamas super().leer() dentro de un método override, Python busca el siguiente método leer en la jerarquía de clases según el MRO y lo invoca, devolviendo su resultado; no transforma datos por sí mismo.​

Llamar super() sin argumentos en Python 3 equivale a super(class, self) dentro del cuerpo de la clase, por eso puedes usarlo “sin declararlo” y funciona con herencia simple o múltiple respetando el MRO.​

Aplicado al Decorator
En tu decorador, super().leer() delega en el siguiente eslabón de la cadena (el decorador base que a su vez llama al objeto envuelto), y luego tu decorador añade su propia lógica como strip() o upper(); super() solo encadena la llamada.​


"""

