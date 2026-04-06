**Explicación:** Antes de separar en servidores, separamos las responsabilidades en archivos. Es un "Monolito Modular".

**Patrón de Diseño:** Fachada (Facade). Un archivo main.py sirve como único punto de entrada, pero delega el trabajo a otros archivos.

**Código:**

1. productos.py: Tiene una clase Catalogo.

2. pedidos.py: Tiene una clase Procesador.

3. main.py: Importa ambos y los expone.

**Ventaja Práctica:** El código es más limpio y fácil de leer.

**Desventaja:** Si main.py falla, todo el sistema sigue cayendo (Sigue siendo un solo proceso).