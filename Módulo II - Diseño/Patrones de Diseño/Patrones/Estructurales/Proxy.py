""" 
Idea en una frase
El cliente usa el proxy como si fuera el servicio; el proxy decide cuándo crear/llamar al objeto real y puede ejecutar acciones antes o después de delegar la solicitud, manteniendo la misma interfaz para que sean intercambiables.​

Ejemplo claro en Python 3.8+
Escenario: un cargador de archivos pesados (simulado) se crea y lee lentamente; el proxy retrasa la creación hasta el primer uso y añade caché.

"""

import time

# Interfaz del servicio
class LectorArchivo:
    def leer(self) -> str:
        raise NotImplementedError

# Servicio real (costoso)
class LectorArchivoReal(LectorArchivo):
    def __init__(self, ruta: str):
        # Simula construcción pesada
        print("Inicializando lector real...")
        time.sleep(1)
        self.ruta = ruta
        self._contenido = None

    def leer(self) -> str:
        if self._contenido is None:
            print("Leyendo del disco...")
            time.sleep(1)
            self._contenido = f"Contenido de {self.ruta}"
        return self._contenido

# Proxy: misma interfaz + control de acceso y caché
class LectorArchivoProxy(LectorArchivo):
    def __init__(self, ruta: str):
        self.ruta = ruta
        self._real = None
        self._cache = None

    def _asegurar_real(self):
        if self._real is None:
            self._real = LectorArchivoReal(self.ruta)

    def leer(self) -> str:
        # Política: caché de contenido
        if self._cache is None:
            print("Proxy: preparando acceso y habilitando caché")
            self._asegurar_real()
            self._cache = self._real.leer()
        else:
            print("Proxy: devolviendo desde caché")
        return self._cache

if __name__ == "__main__":
    lector = LectorArchivoProxy("reporte.txt")
    print(lector.leer())   # primera vez: inicializa y lee
    print(lector.leer())   # segunda vez: usa caché
