class ModuloProductos:
    def __init__(self):
        # La "Base de datos" ahora es privada de este módulo
        self._db = {
            1: {"nombre": "Laptop", "precio": 1000},
            2: {"nombre": "Mouse", "precio": 20}
        }

    def obtener_todo(self):
        return self._db

    def validar_existencia(self, id_prod):
        return id_prod in self._db