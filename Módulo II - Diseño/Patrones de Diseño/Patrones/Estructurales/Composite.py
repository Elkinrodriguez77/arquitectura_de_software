"""
Ejemplo: 
Un carrito de compras con productos individuales y “paquetes” que contienen productos o más paquetes.
"""

from abc import ABC, abstractmethod
from typing import List

# Interfaz común
class Item(ABC):
    @abstractmethod
    def precio(self) -> float:
        pass

# Hoja
class Producto(Item):
    def __init__(self, nombre: str, costo: float):
        self.nombre = nombre
        self.costo = costo

    def precio(self) -> float:
        return self.costo

# Compuesto
class Paquete(Item):
    def __init__(self, nombre: str):
        self.nombre = nombre
        self._items = []  # type: List[Item]

    def agregar(self, item: Item) -> None:
        self._items.append(item)

    def precio(self) -> float:
        # Suma recursiva de todos los hijos
        return sum(item.precio() for item in self._items)

# ---- Ejecución de ejemplo ----
if __name__ == "__main__":
    libro = Producto("Libro", 30.0)
    lapiz = Producto("Lápiz", 2.0)

    promo_escolar = Paquete("Promo escolar")
    promo_escolar.agregar(libro)
    promo_escolar.agregar(lapiz)

    mega_combo = Paquete("Mega combo")
    mega_combo.agregar(promo_escolar)   # paquete dentro de paquete
    mega_combo.agregar(Producto("Mochila", 25.0))

    carrito = [lapiz, mega_combo]  # type: List[Item]
    total = sum(i.precio() for i in carrito)
    print(f"Total: {total}")

