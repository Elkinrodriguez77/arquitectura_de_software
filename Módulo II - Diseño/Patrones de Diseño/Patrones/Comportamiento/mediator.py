"""
USO:
python mediator.py
Coordina componentes (chat simple) a través de un mediador central.
"""
class Chat:
    def __init__(self): self.usuarios = []
    def registrar(self, u): self.usuarios.append(u); u.chat = self
    def enviar(self, emisor, msg):
        for u in self.usuarios:
            if u is not emisor: u.recibir(emisor.nombre, msg)

class Usuario:
    def __init__(self, nombre): self.nombre, self.chat = nombre, None
    def enviar(self, msg): self.chat.enviar(self, msg)
    def recibir(self, de, msg): print(f"{self.nombre} recibe de {de}: {msg}")

if __name__ == "__main__":
    chat = Chat()
    ana, bob = Usuario("Ana"), Usuario("Bob")
    chat.registrar(ana); chat.registrar(bob)
    ana.enviar("Hola, Bob")
