from abc import ABC, abstractmethod

# --- 1. INTERFACES SEGREGADAS (ISP) ---
# En lugar de una interfaz gigante, hacemos dos pequeñas.
class ITrabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class IComensal(ABC):
    @abstractmethod
    def comer(self):
        pass

# --- 2. CLASES QUE CUMPLEN LOS CONTRATOS ---
class CocineroHumano(ITrabajador, IComensal):
    def trabajar(self):
        print("👨‍🍳 Cocinando a toda velocidad.")
        
    def comer(self):
        print("🍔 Tomando un descanso para comer.")

class RobotLimpiador(ITrabajador):
    # El robot solo hereda ITrabajador, ¡ya no lo obligamos a comer!
    def trabajar(self):
        print("🤖 Limpiando el suelo automáticamente.")

# --- 3. EL PROBLEMA EXTERNO ---
# Compramos este robot de otra empresa y NO podemos editar su código:
class RobotAvanzadoExterno:
    def iniciar_bateria_y_limpiar(self):
        print("🛸 [SISTEMA EXTERNO] Escaneando área y aspirando...")

# --- 4. PATRÓN ADAPTER ---
# Creamos un adaptador para que el robot externo encaje en nuestro restaurante
class AdaptadorRobot(ITrabajador):
    def __init__(self, robot_externo: RobotAvanzadoExterno):
        self.robot_externo = robot_externo
        
    def trabajar(self):
        # Traducimos la orden estándar a la orden que el robot entiende
        self.robot_externo.iniciar_bateria_y_limpiar()

# --- 5. PRUEBA DEL SISTEMA ---
if __name__ == "__main__":
    print("--- Gestión de Personal del Restaurante ---")
    
    # Nuestro personal normal
    pedro = CocineroHumano()
    robot_basico = RobotLimpiador()
    
    # El nuevo robot de otra marca, envuelto en su adaptador
    robot_raro = RobotAvanzadoExterno()
    robot_adaptado = AdaptadorRobot(robot_raro)
    
    # Todos trabajan usando el MISMO comando, gracias al adaptador y las interfaces
    equipo = [pedro, robot_basico, robot_adaptado]
    
    for miembro in equipo:
        miembro.trabajar()
        
    print("\n--- Hora del descanso ---")
    # Solo Pedro come, los robots no están obligados a tener este método
    pedro.comer()