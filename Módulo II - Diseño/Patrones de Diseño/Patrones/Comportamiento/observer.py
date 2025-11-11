"""
USO:
python observer.py
Suscripción/notificación de cambios (publicador-suscriptor).
"""
class Subject:
    def __init__(self): self.obs = []
    def suscribir(self, o): self.obs.append(o)
    def notificar(self, dato):
        for o in self.obs: o.update(dato)

class Logger:
    def update(self, dato): print("LOG:", dato)

if __name__ == "__main__":
    s = Subject(); s.suscribir(Logger())
    s.notificar("Evento X")
