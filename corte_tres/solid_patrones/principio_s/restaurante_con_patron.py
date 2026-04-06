# 1. Aplicamos SRP: Cada clase tiene una única responsabilidad

class Cocinero:
    def cocinar_plato(self, plato):
        print(f"👨‍🍳 Cocinando: {plato}")

class Cajero:
    def procesar_pago(self, monto):
        print(f"💳 Procesando pago de ${monto}")

class Bodeguero:
    def actualizar_inventario(self, plato):
        print(f"📦 Descontando ingredientes de {plato}")

# 2. Aplicamos Patrón Facade: Una interfaz simple que coordina a los especialistas

class Restaurante:
    def __init__(self):
        # El restaurante "contrata" a sus especialistas
        self.cocinero = Cocinero()
        self.cajero = Cajero()
        self.bodeguero = Bodeguero()

    def atender_cliente(self, plato, monto):
        # El cliente solo habla con el Restaurante (la fachada)
        # El Restaurante delega el trabajo pesado a los especialistas
        self.cocinero.cocinar_plato(plato)
        self.cajero.procesar_pago(monto)
        self.bodeguero.actualizar_inventario(plato)
        print("✅ Orden completada")

# Probémoslo:
mi_restaurante = Restaurante()
mi_restaurante.atender_cliente("Pizza", 20)