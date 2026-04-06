from abc import ABC, abstractmethod

# --- 1. ESTRATEGIAS DE PAGO (OCP - Abierto/Cerrado) ---
class MetodoPago(ABC):
    @abstractmethod
    def pagar(self, monto):
        pass

class PagoTarjeta(MetodoPago):
    def pagar(self, monto):
        print(f"💳 Cobrando ${monto} con Tarjeta")

class PagoPayPal(MetodoPago):
    def pagar(self, monto):
        print(f"📱 Cobrando ${monto} con PayPal")

# --- 2. ESPECIALISTAS (SRP - Responsabilidad Única) ---
class Cocinero:
    def cocinar_plato(self, plato):
        print(f"👨‍🍳 Cocinando: {plato}")

class Bodeguero:
    def actualizar_inventario(self, plato):
        print(f"📦 Descontando ingredientes de {plato}")

class Cajero:
    # El cajero delega el cobro a la estrategia que reciba
    def procesar_pago(self, monto, estrategia_pago: MetodoPago):
        estrategia_pago.pagar(monto)

# --- 3. FACHADA (Patrón Facade) ---
class Restaurante:
    def __init__(self):
        self.cocinero = Cocinero()
        self.cajero = Cajero()
        self.bodeguero = Bodeguero()

    # Añadimos la estrategia como parámetro
    def atender_cliente(self, plato, monto, estrategia_pago: MetodoPago):
        self.cocinero.cocinar_plato(plato)
        # Pasamos la estrategia al cajero
        self.cajero.procesar_pago(monto, estrategia_pago)
        self.bodeguero.actualizar_inventario(plato)
        print("✅ Orden completada\n")

# --- 4. PRUEBA DEL SISTEMA UNIFICADO ---
mi_restaurante = Restaurante()

print("--- Cliente 1 ---")
pago_1 = PagoTarjeta()
mi_restaurante.atender_cliente("Pizza", 20, pago_1)

print("--- Cliente 2 ---")
pago_2 = PagoPayPal()
mi_restaurante.atender_cliente("Hamburguesa", 15, pago_2)