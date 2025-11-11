"""
Escenario: generar un reporte PDF sencillo requiere varios pasos (cargar datos, formatear, renderizar); la fachada expone un único método crear_reporte_pdf. 
"""

# --- Subsistema complejo ---
class CargadorDatos:
    def cargar(self, fuente: str):
        # Aquí iría lectura de CSV/DB/API
        return [{"cliente": "Ana", "total": 59}, {"cliente": "Luis", "total": 42}]

class Formateador:
    def tabla(self, registros):
        # Convierte a una tabla simple (string)
        cabecera = "Cliente | Total\n"
        filas = "\n".join(f"{r['cliente']} | {r['total']}" for r in registros)
        return cabecera + filas

class RenderPDF:
    def render(self, contenido: str, archivo: str):
        # Simula PDF; en la vida real usarías una librería como ReportLab
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(f"PDF\n----\n{contenido}")

# --- Fachada ---
class ReportesFacade:
    def __init__(self):
        self.loader = CargadorDatos()
        self.formatter = Formateador()
        self.pdf = RenderPDF()

    def crear_reporte_pdf(self, fuente: str, archivo_salida: str) -> None:
        datos = self.loader.cargar(fuente)
        contenido = self.formatter.tabla(datos)
        self.pdf.render(contenido, archivo_salida)

# --- Cliente ---
if __name__ == "__main__":
    fachada = ReportesFacade()
    fachada.crear_reporte_pdf("ventas.csv", "reporte.pdf")
    print("Reporte generado")
