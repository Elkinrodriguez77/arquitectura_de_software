
from abc import ABC, abstractmethod

# 1. Definimos el "contrato" o la Estrategia (Interfaz)
class MetodoPago(ABC):
    @abstractmethod
    def pagar(self, monto):
        pass

# 2. Creamos las estrategias concretas (Extensiones)
class PagoTarjeta(MetodoPago):
    def pagar(self, monto):
        print(f"💳 Cobrando ${monto} con Tarjeta")

class PagoPayPal(MetodoPago):
    def pagar(self, monto):
        print(f"📱 Cobrando ${monto} con PayPal")

# 3. El Cajero ahora está "Cerrado" a modificaciones. Solo recibe una estrategia.
class Cajero:
    def procesar_pago(self, monto, estrategia_pago: MetodoPago):
        estrategia_pago.pagar(monto)

# Probémoslo:
mi_cajero = Cajero()

pago_cliente_1 = PagoTarjeta()
mi_cajero.procesar_pago(50, pago_cliente_1)

pago_cliente_2 = PagoPayPal()
mi_cajero.procesar_pago(30, pago_cliente_2)