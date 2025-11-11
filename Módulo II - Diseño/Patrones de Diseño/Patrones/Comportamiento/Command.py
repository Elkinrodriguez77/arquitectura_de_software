"""
USO:
python command.py
Encapsula operaciones como objetos para deshacer/rehacer y colas.
"""
from abc import ABC, abstractmethod

class Documento:
    def __init__(self):
        self.texto = ""
    def insertar(self, t): self.texto += t
    def borrar(self, n): 
        borrado = self.texto[-n:]
        self.texto = self.texto[:-n]
        return borrado

class Command(ABC):
    @abstractmethod
    def ejecutar(self): ...
    @abstractmethod
    def deshacer(self): ...

class InsertarTexto(Command):
    def __init__(self, doc, t): self.doc, self.t = doc, t
    def ejecutar(self): self.doc.insertar(self.t)
    def deshacer(self): self.doc.borrar(len(self.t))

class Invocador:
    def __init__(self): self.hist = []
    def run(self, cmd):
        cmd.ejecutar(); self.hist.append(cmd)
    def undo(self):
        if self.hist: self.hist.pop().deshacer()

if __name__ == "__main__":
    d = Documento(); inv = Invocador()
    inv.run(InsertarTexto(d, "Hola "))
    inv.run(InsertarTexto(d, "Mundo"))
    print(d.texto)      # Hola Mundo
    inv.undo()
    print(d.texto)      # Hola 
