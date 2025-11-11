"""
USO:
python strategy.py
Selecciona algoritmos intercambiables en tiempo de ejecución.
"""
from abc import ABC, abstractmethod

class Estrategia(ABC):
    @abstractmethod
    def enviar(self, total): ...

class EnvioBarato(Estrategia):
    def enviar(self, total): return 5.0

class EnvioExpress(Estrategia):
    def enviar(self, total): return 15.0 if total < 50 else 10.0

class Checkout:
    def __init__(self, estrategia: Estrategia):
        self.estrategia = estrategia
    def costo_envio(self, total):
        return self.estrategia.enviar(total)

if __name__ == "__main__":
    print(Checkout(EnvioBarato()).costo_envio(30))
    print(Checkout(EnvioExpress()).costo_envio(30))
