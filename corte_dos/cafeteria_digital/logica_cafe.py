# Patrón de Diseño: Factory
# Este código se encarga solo de "CÓMO" fabricar un objeto café.

class Cafe:
    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes

class FabricaDeCafe:
    ## @staticmethod
    def preparar_cafe(tipo):
        if tipo == "espresso":
            return Cafe("Espresso", "Agua y Café molido")
        elif tipo == "latte":
            return Cafe("Latte", "Café, Leche espumosa y vapor")
        else:
            return Cafe("Café de la casa", "Granos seleccionados")