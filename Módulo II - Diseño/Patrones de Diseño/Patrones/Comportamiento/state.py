"""
USO:
python state.py
Cambia comportamiento según el estado actual sin if/else gigantes.
"""
from abc import ABC, abstractmethod

class Estado(ABC):
    @abstractmethod
    def reproducir(self, ctx): ...

class EnPausa(Estado):
    def reproducir(self, ctx):
        print("Reanudando"); ctx.estado = Reproduciendo()

class Reproduciendo(Estado):
    def reproducir(self, ctx):
        print("Pausando"); ctx.estado = EnPausa()

class Reproductor:
    def __init__(self): self.estado = EnPausa()
    def click_play(self): self.estado.reproducir(self)

if __name__ == "__main__":
    r = Reproductor()
    r.click_play(); r.click_play()
