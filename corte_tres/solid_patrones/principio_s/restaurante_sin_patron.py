class Restaurante:
    def cocinar_plato(self, plato):
        print(f"👨‍🍳 Cocinando: {plato}")

    def procesar_pago(self, monto):
        print(f"💳 Cobrando ${monto} con tarjeta de crédito")

    def actualizar_inventario(self, plato):
        print(f"📦 Descontando ingredientes de {plato}")

    def atender_cliente(self, plato, monto):
        self.cocinar_plato(plato)
        self.procesar_pago(monto)
        self.actualizar_inventario(plato)
        print("✅ Orden completada")

# Probémoslo:
mi_restaurante = Restaurante()
mi_restaurante.atender_cliente("Hamburguesa", 15)