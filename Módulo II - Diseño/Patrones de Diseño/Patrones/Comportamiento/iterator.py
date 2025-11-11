"""
USO:
python iterator.py
Itera una colección personalizada sin exponer su representación interna.
"""
class Coleccion:
    def __init__(self, datos): self._datos = list(datos)
    def __iter__(self):
        i = 0
        while i < len(self._datos):
            yield self._datos[i]
            i += 1

if __name__ == "__main__":
    for x in Coleccion([1,2,3]): 
        print(x)
