""" 
Caso: íconos en un mapa con miles de puntos. Todos los taxis amarillos comparten la misma imagen y tamaño (intrínseco); la posición y etiqueta cambian (extrínseco).
"""

from typing import Dict, Tuple

# Flyweight: guarda solo el estado intrínseco (compartido)
class Icono:
    def __init__(self, tipo: str, color: str, pixmap: bytes):
        self.tipo = tipo          # intrínseco compartido
        self.color = color        # intrínseco compartido
        self.pixmap = pixmap      # intrínseco compartido (simula la imagen)

    # El estado extrínseco se pasa en cada uso
    def dibujar(self, x: int, y: int, etiqueta: str) -> None:
        print(f"{self.tipo}-{self.color} en ({x},{y}) -> {etiqueta}")

# Fábrica: garantiza reutilización por clave de estado intrínseco
class IconoFactory:
    _pool: Dict[Tuple[str, str], Icono] = {}

    @classmethod
    def obtener(cls, tipo: str, color: str) -> Icono:
        clave = (tipo, color)
        if clave not in cls._pool:
            # En un caso real, cargaría/crearía el bitmap una sola vez
            cls._pool[clave] = Icono(tipo, color, pixmap=b"...imagen...")
        return cls._pool[clave]

# Cliente: crea muchos "marcadores" ligeros
if __name__ == "__main__":
    taxis_amarillos = [ (10, 5, "TX-001"),
                        (11, 6, "TX-002"),
                        (12, 7, "TX-003") ]

    bus_rojo = [ (20, 8, "BUS-21"), (21, 9, "BUS-22") ]

    icono_taxi = IconoFactory.obtener("taxi", "amarillo")
    for x, y, tag in taxis_amarillos:
        icono_taxi.dibujar(x, y, tag)

    icono_bus = IconoFactory.obtener("bus", "rojo")
    for x, y, tag in bus_rojo:
        icono_bus.dibujar(x, y, tag)

    # Comprobación de reutilización:
    mismo_icono = IconoFactory.obtener("taxi", "amarillo")
    print("¿Reutiliza instancia?", icono_taxi is mismo_icono)
