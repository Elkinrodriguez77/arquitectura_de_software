"""
USO:
python chain_of_responsibility.py
Demuestra una cadena de validadores donde cada manejador procesa o pasa la solicitud al siguiente.
"""
from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, next_handler=None):
        self.next = next_handler
    def handle(self, req):
        res = self._process(req)
        if res is None and self.next:
            return self.next.handle(req)
        return res
    @abstractmethod
    def _process(self, req): ...

class ValidaNoVacio(Handler):
    def _process(self, req):
        return "Error: vacío" if not req else None

class ValidaLongitud(Handler):
    def _process(self, req):
        return "Error: corto" if len(req) < 3 else None

class ValidaSoloLetras(Handler):
    def _process(self, req):
        return "Error: no letras" if not req.isalpha() else "OK"

if __name__ == "__main__":
    cadena = ValidaNoVacio(ValidaLongitud(ValidaSoloLetras()))
    for r in ["", "ab", "abc", "abc123"]:
        print(r, "->", cadena.handle(r))
