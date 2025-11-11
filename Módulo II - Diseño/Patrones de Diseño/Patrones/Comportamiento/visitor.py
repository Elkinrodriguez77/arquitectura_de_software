"""
USO:
python visitor.py
Añade operaciones a una jerarquía sin modificar sus clases.
"""
from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_texto(self, e): ...
    @abstractmethod
    def visit_num(self, e): ...

class Elemento(ABC):
    @abstractmethod
    def aceptar(self, v: Visitor): ...

class Texto(Elemento):
    def __init__(self, s): self.s = s
    def aceptar(self, v: Visitor): v.visit_texto(self)

class Numero(Elemento):
    def __init__(self, n): self.n = n
    def aceptar(self, v: Visitor): v.visit_num(self)

class ContarCaracteres(Visitor):
    def visit_texto(self, e): print("len texto:", len(e.s))
    def visit_num(self, e): print("len num:", len(str(e.n)))

if __name__ == "__main__":
    elems = [Texto("Hola"), Numero(12345)]
    v = ContarCaracteres()
    for e in elems: e.aceptar(v)
