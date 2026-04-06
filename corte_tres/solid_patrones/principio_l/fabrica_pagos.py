from abc import ABC, abstractmethod

# --- 1. ESTRATEGIAS DE PAGO (OCP y LSP) ---
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

class PagoNequi(MetodoPago):
    def pagar(self, monto):
        print(f"📱 Cobrando ${monto} con Nequi")

# --- 2. FÁBRICA DE PAGOS (Patrón Factory) ---
class FabricaPagos:
    @staticmethod
    def crear_pago(tipo_pago: str):
        if tipo_pago.lower() == "tarjeta":
            return PagoTarjeta()
        elif tipo_pago.lower() == "paypal":
            return PagoPayPal()
        elif tipo_pago.lower() == "nequi":
            return PagoNequi()
        else:
            raise ValueError(f"❌ El método de pago '{tipo_pago}' no existe en nuestra fábrica.")

# --- 3. ESPECIALISTAS (SRP - Responsabilidad Única) ---
class Cocinero:
    def cocinar_plato(self, plato):
        print(f"👨‍🍳 Cocinando: {plato}")

class Bodeguero:
    def actualizar_inventario(self, plato):
        print(f"📦 Descontando ingredientes de {plato}")

class Cajero:
    def procesar_pago(self, monto, estrategia_pago: MetodoPago):
        estrategia_pago.pagar(monto)

# --- 4. FACHADA (Patrón Facade) ---
class Restaurante:
    def __init__(self):
        self.cocinero = Cocinero()
        self.cajero = Cajero()
        self.bodeguero = Bodeguero()

    def atender_cliente(self, plato, monto, estrategia_pago: MetodoPago):
        self.cocinero.cocinar_plato(plato)
        self.cajero.procesar_pago(monto, estrategia_pago)
        self.bodeguero.actualizar_inventario(plato)
        print("✅ Orden completada\n")

# --- 5. PRUEBA DEL SISTEMA COMPLETO CON INPUT ---
if __name__ == "__main__":
    print("--- Bienvenidos al Restaurante SOLID ---")
    mi_restaurante = Restaurante()
    
    # Usamos un ciclo simple para atender a varios clientes
    while True:
        seleccion_cliente = input("Ingrese método de pago (tarjeta/paypal/nequi) o 'salir' para cerrar: ")
        
        if seleccion_cliente.lower() == 'salir':
            print("Cerrando el restaurante. ¡Hasta pronto!")
            break
            
        try:
            # Intentamos crear el pago con lo que el usuario escribió
            metodo_elegido = FabricaPagos.crear_pago(seleccion_cliente)
            mi_restaurante.atender_cliente("Tacos", 12, metodo_elegido)
        except ValueError as error:
            # Si la fábrica lanza un error, lo mostramos sin detener el programa
            print(error)
            print("Por favor, intente con un método válido.\n")