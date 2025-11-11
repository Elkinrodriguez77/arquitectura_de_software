""" 
Ejemplo:
Supón que quieres enviar notificaciones por distintos canales (email y SMS) y con diferentes tipos de aviso (alerta y recordatorio); Bridge evita crear combinaciones como AlertaEmail, AlertaSMS, RecordatorioEmail, RecordatorioSMS, separando “tipo de notificación” de “canal”.
"""

# Implementación: define la interfaz común de los canales
class CanalNotificacion:
    def enviar(self, destino: str, mensaje: str) -> None:
        raise NotImplementedError

class CanalEmail(CanalNotificacion):
    def enviar(self, destino: str, mensaje: str) -> None:
        print(f"[EMAIL] a {destino}: {mensaje}")

class CanalSMS(CanalNotificacion):
    def enviar(self, destino: str, mensaje: str) -> None:
        print(f"[SMS] a {destino}: {mensaje}")

# Abstracción: lógica de alto nivel que usa un canal
class Notificacion:
    def __init__(self, canal: CanalNotificacion):
        self.canal = canal

    def enviar(self, destino: str, mensaje: str) -> None:
        self.canal.enviar(destino, mensaje)

# Abstracciones refinadas: distintos comportamientos de negocio
class Alerta(Notificacion):
    def enviar(self, destino: str, mensaje: str) -> None:
        super().enviar(destino, f"ALERTA: {mensaje}")

class Recordatorio(Notificacion):
    def enviar(self, destino: str, mensaje: str) -> None:
        super().enviar(destino, f"Recordatorio: {mensaje}")

# Uso: combinaciones libres sin crear nuevas clases por cada par
email = CanalEmail()
sms = CanalSMS()

alerta_email = Alerta(email)
alerta_email.enviar("ana@acme.com", "CPU > 90%")

recordatorio_sms = Recordatorio(sms)
recordatorio_sms.enviar("+573001234567", "Reunión 3 PM")


""" 
Agregar un nuevo canal como Push o WhatsApp no obliga a tocar Alerta/Recordatorio, y añadir un nuevo tipo de notificación no obliga a cambiar CanalEmail/SMS, cumpliendo abierto/cerrado y responsabilidad única típicos del Bridge.
"""