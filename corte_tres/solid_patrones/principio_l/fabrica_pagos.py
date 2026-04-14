from abc import ABC, abstractmethod

# --- 1. ESTRATEGIAS DE PAGO (LSP se cumple aquí) ---
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

# 🌟 NUEVO PAGO: Creamos la clase
class PagoBitcoin(MetodoPago):
    def pagar(self, monto):
        print(f"🪙 Cobrando ${monto} con Bitcoin")

# --- 2. FÁBRICA DE PAGOS  ---
class FabricaPagos:
    # Diccionario que asocia: Número -> (Nombre para el menú, Clase a instanciar)
    _metodos = {
        "1": ("Tarjeta", PagoTarjeta),
        "2": ("PayPal", PagoPayPal),
        "3": ("Nequi", PagoNequi)
    }

    @classmethod
    def registrar_nuevo_metodo(cls, opcion_numero: str, nombre: str, clase_metodo):
        """Permite agregar nuevos pagos dinámicamente sin modificar esta clase"""
        cls._metodos[opcion_numero] = (nombre, clase_metodo)

    @classmethod
    def mostrar_menu(cls):
        opciones = [f"{num}. {datos[0]}" for num, datos in cls._metodos.items()]
        return " | ".join(opciones)

    @classmethod
    def crear_pago(cls, opcion: str):
        if opcion in cls._metodos:
            clase_pago = cls._metodos[opcion][1]
            return clase_pago() # Retorna la instancia de la clase
        else:
            raise ValueError(f"❌ La opción '{opcion}' no es válida.")

# 🌟 REGISTRAMOS EL NUEVO PAGO EN LA FÁBRICA
FabricaPagos.registrar_nuevo_metodo("4", "Bitcoin", PagoBitcoin)

# --- 3. ESPECIALISTAS (SRP - Responsabilidad Única) ---
class Cocinero:
    def cocinar_plato(self, plato):
        print(f"👨‍🍳 Cocinando: {plato}")

class Bodeguero:
    def actualizar_inventario(self, plato):
        print(f"📦 Descontando ingredientes de {plato}")

class Cajero:
    # 🌟 LSP en acción: El cajero recibe la abstracción (MetodoPago), no la clase concreta.
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
    
    while True:
        print(f"\n{FabricaPagos.mostrar_menu()} | S. Salir")
        seleccion_cliente = input("Ingrese el número de su método de pago: ")
        
        if seleccion_cliente.lower() == 's':
            print("Cerrando el restaurante. ¡Hasta pronto!")
            break
            
        try:
            metodo_elegido = FabricaPagos.crear_pago(seleccion_cliente)
            mi_restaurante.atender_cliente("Tacos", 12, metodo_elegido)
        except ValueError as error:
            print(error)
            print("Por favor, intente con una opción válida.")