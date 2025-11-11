"""
USO:
python template_method.py
Fija el esqueleto de un proceso y permite a subclases redefinir pasos.
"""
from abc import ABC, abstractmethod

class Reporte(ABC):
    def generar(self):
        datos = self.cargar()
        contenido = self.formatear(datos)
        self.exportar(contenido)
    @abstractmethod
    def cargar(self): ...
    @abstractmethod
    def formatear(self, datos): ...
    @abstractmethod
    def exportar(self, contenido): ...

class ReporteVentasTXT(Reporte):
    def cargar(self): return [{"c":"Ana","t":59},{"c":"Luis","t":42}]
    def formatear(self, datos):
        return "\n".join(f"{r['c']}: {r['t']}" for r in datos)
    def exportar(self, contenido): print(contenido)

if __name__ == "__main__":
    ReporteVentasTXT().generar()
