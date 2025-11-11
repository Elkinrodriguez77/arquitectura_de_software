"""
USO:
python memento.py
Guarda y restaura el estado sin exponer detalles internos.
"""
class Editor:
    def __init__(self): self.texto = ""
    def escribir(self, t): self.texto += t
    def crear_memento(self): return self.texto
    def restaurar(self, m): self.texto = m

if __name__ == "__main__":
    ed = Editor()
    ed.escribir("Hola "); punto = ed.crear_memento()
    ed.escribir("Mundo")
    print(ed.texto)        # Hola Mundo
    ed.restaurar(punto)
    print(ed.texto)        # Hola 
