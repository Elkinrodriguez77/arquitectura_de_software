from abc import ABC, abstractmethod

# ==========================================
# 1. ABSTRACCIONES (Interfaces para DIP e ISP)
# ==========================================
class MetodoPago(ABC):
    @abstractmethod
    def pagar(self, monto): pass

class ICocinero(ABC):
    @abstractmethod
    def cocinar_plato(self, plato): pass

class ICajero(ABC):
    @abstractmethod
    def procesar_pago(self, monto, estrategia: MetodoPago): pass

class IBodeguero(ABC):
    @abstractmethod
    def actualizar_inventario(self, plato): pass

# ==========================================
# 2. IMPLEMENTACIONES DE BAJO NIVEL (SRP, OCP, LSP)
# ==========================================
class PagoTarjeta(MetodoPago):
    def pagar(self, monto):
        print(f"💳 Cobrando ${monto} con Tarjeta")

class PagoPayPal(MetodoPago):
    def pagar(self, monto):
        print(f"📱 Cobrando ${monto} con PayPal")

class FabricaPagos:
    @staticmethod
    def crear_pago(tipo_pago: str):
        if tipo_pago.lower() == "tarjeta": return PagoTarjeta()
        elif tipo_pago.lower() == "paypal": return PagoPayPal()
        else: raise ValueError(f"❌ Método '{tipo_pago}' no existe.")

class CocineroExperto(ICocinero):
    def cocinar_plato(self, plato):
        print(f"👨‍🍳 Cocinando {plato} a la perfección.")

class CajeroHumano(ICajero):
    def procesar_pago(self, monto, estrategia: MetodoPago):
        estrategia.pagar(monto)

class BodegueroHumano(IBodeguero):
    def actualizar_inventario(self, plato):
        print(f"📦 Descontando ingredientes para {plato}.")

# ==========================================
# 3. MÓDULO DE ALTO NIVEL (Patrón Facade + DIP)
# ==========================================
class Restaurante:
    # INYECCIÓN DE DEPENDENCIAS: El restaurante exige trabajadores certificados (interfaces)
    def __init__(self, cocinero: ICocinero, cajero: ICajero, bodeguero: IBodeguero):
        self.cocinero = cocinero
        self.cajero = cajero
        self.bodeguero = bodeguero

    def atender_cliente(self, plato, monto, estrategia_pago: MetodoPago):
        self.cocinero.cocinar_plato(plato)
        self.cajero.procesar_pago(monto, estrategia_pago)
        self.bodeguero.actualizar_inventario(plato)
        print("✅ Orden completada\n")

# ==========================================
# 4. PRUEBA FINAL (Ensamblaje del sistema)
# ==========================================
if __name__ == "__main__":
    print("--- Ensamblando el Restaurante SOLID ---")
    
    # 1. Creamos a los trabajadores por fuera (Bajo Nivel)
    chef_pedro = CocineroExperto()
    cajera_ana = CajeroHumano()
    bodeguero_luis = BodegueroHumano()
    
    # 2. Inyectamos las dependencias al Restaurante (Alto Nivel)
    mi_restaurante = Restaurante(chef_pedro, cajera_ana, bodeguero_luis)
    
    # 3. El cliente interactúa
    print("--- Atendiendo Cliente ---")
    metodo_cliente = FabricaPagos.crear_pago("tarjeta")
    mi_restaurante.atender_cliente("Pasta", 25, metodo_cliente)