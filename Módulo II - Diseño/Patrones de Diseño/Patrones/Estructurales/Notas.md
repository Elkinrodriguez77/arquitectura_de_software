# **Patrones de Diseño**

En la práctica nadie usa “el 100%” de los patrones ni intenta forzarlos siempre; se aplican solo cuando resuelven un problema real y aportan simplicidad, claridad o extensibilidad al diseño.​

## Cómo se usan en la vida real

- Los patrones son soluciones probadas y un lenguaje común del equipo; ayudan a comunicar ideas y a reutilizar enfoques, pero no son recetas obligatorias ni se memorizan todos los detalles de implementación.​
- Se elige un patrón cuando aparece el problema típico que aborda; por ejemplo, Observer para notificaciones, Strategy para alternativas de algoritmo, o Facade para simplificar un subsistema complejo, evitando sobreingeniería si una solución simple basta.​

## Recomendaciones prácticas

- Empieza simple y refactoriza hacia un patrón cuando surja la necesidad: si crece el acoplamiento, falta extensibilidad o hay duplicación, un patrón puede estabilizar el diseño sin complicarlo de más.​
- Conoce los patrones comunes de cada categoría (creacionales, estructurales, de comportamiento) y sus casos de uso típicos, para reconocer cuándo encajan y cuándo no; usarlos bien suele mejorar mantenibilidad y calidad del software.​

# **Patrones Estructurales:**

## **1. Adapter**

### Propósito

Adapter es un patrón de diseño estructural que permite la colaboración entre objetos con interfaces incompatibles.

### Cuándo conviene

- Reutilizar clases existentes con interfaces que no se pueden cambiar, evitando duplicar código o modificar librerías de terceros.​
- Incorporar gradualmente componentes antiguos a sistemas nuevos, envolviéndolos sin tocar su código fuente.​

### Ventajas y notas

- Permite introducir nuevos adaptadores sin tocar el código cliente, mejorando extensibilidad y evitando romper dependencias.​

Se diferencia de Decorator porque cambia la interfaz expuesta, mientras Decorator la mantiene y solo añade responsabilidades; Bridge suele planearse desde el diseño, mientras Adapter se aplica para integrar algo ya existente.

## **2. Bridge**

### Propósito

El patrón Bridge separa “qué se hace” de “cómo se hace” creando dos jerarquías: una de abstracciones y otra de implementaciones intercambiables, lo que evita la explosión de subclases y permite evolucionarlas por separado.​

- Idea en una frase:
  La abstracción mantiene una referencia a una implementación y delega en ella el trabajo específico, formando un “puente” entre ambas jerarquías para variar cada una de manera independiente sin romper a la otra.

### Cuándo usarlo

- Cuando una clase tiene variaciones en dos dimensiones independientes y la herencia produce combinaciones explosivas, como formas/colores, GUI/SO o tipos de notificación/canales.​
- Cuando se necesita cambiar implementaciones en tiempo de ejecución pasando otro objeto de implementación al constructor de la abstracción sin modificar el código cliente existente.​

### Ventajas clave

- Reduce el acoplamiento, facilita pruebas y mantenimiento, y permite añadir nuevas implementaciones o abstracciones sin tocar el resto del sistema, evitando efectos colaterales en plataformas o proveedores distintos.​
- Resulta útil en escenarios multiplataforma, múltiples proveedores de API o diversas backends de datos, manteniendo al cliente trabajando con interfaces de alto nivel.

## **3. Composite**

También llamado: Objeto compuesto, Object Tree

### Propósito

Composite es un patrón de diseño estructural que te permite componer objetos en estructuras de árbol y trabajar con esas estructuras como si fueran objetos individuales.

### Cuándo usarlo

- Cuando tu dominio se modela naturalmente como jerarquías parte-todo, como sistemas de archivos, gráficos de UI, menús o carritos con paquetes y subpaquetes.​
- Cuando quieres que el código cliente sea simple y uniforme, evitando if/else para diferenciar entre elementos simples y compuestos gracias a la misma interfaz.​

### Ventajas clave

- Permite añadir nuevas clases hoja o compuestas sin cambiar el cliente, favoreciendo extensibilidad y operaciones agregadas como conteos, sumas o búsquedas.​
- Facilita recorridos recursivos y reduce acoplamiento, ya que los compuestos contienen componentes por la interfaz común y no por tipos concretos.​

## **Decorator**

También llamado: Decorador, Envoltorio, Wrapper

### Propósito

Decorator es un patrón de diseño estructural que te permite añadir funcionalidades a objetos colocando estos objetos dentro de objetos encapsuladores especiales que contienen estas funcionalidades.

### Cuándo usarlo

- Cuando necesites añadir o combinar funcionalidades opcionales a instancias específicas en tiempo de ejecución sin heredar múltiples variantes ni modificar la clase original.​
- Cuando requieras mantener una interfaz común para que el resto del sistema no note si trabaja con el objeto “puro” o con uno decorado con varias capas.​

### Diferencias clave

- A diferencia de Adapter, aquí la interfaz no cambia; simplemente se extiende el comportamiento manteniendo la misma firma y permitiendo apilar múltiples wrappers recursivamente.​
- Aunque Decorator y Proxy se parecen estructuralmente, Decorator busca añadir responsabilidades, mientras Proxy controla el acceso o añade políticas alrededor del objeto original.

## **Facade**

También llamado: Fachada

### Propósito

Facade es un patrón de diseño estructural que proporciona una interfaz simplificada a una biblioteca, un framework o cualquier otro grupo complejo de clases.

### Cuándo usarlo

- Cuando un módulo o librería tiene muchas clases y secuencias de inicialización, y el cliente solo requiere un conjunto de operaciones frecuentes y bien definidas.​
- Para definir puntos de entrada a capas: una fachada por capa minimiza dependencias entre subsistemas y hace más fácil sustituir componentes internos en el futuro.​

### Diferencias rápidas

-- Adapter cambia la interfaz de un único componente para que encaje con el cliente; Facade ofrece una interfaz simple sobre varios componentes de un subsistema completo.​
-- Proxy mantiene la misma interfaz del servicio y controla el acceso; la fachada no pretende ser intercambiable con el subsistema, solo lo simplifica para el cliente.

## Flyweight

También llamado: Peso mosca, Peso ligero, Cache

### Propósito

Flyweight es un patrón de diseño estructural que te permite mantener más objetos dentro de la cantidad disponible de RAM compartiendo las partes comunes del estado entre varios objetos en lugar de mantener toda la información en cada objeto.

### Cuándo usarlo

- Cuando hay un gran número de objetos similares y el coste de memoria es alto, como árboles en un bosque, caracteres con misma fuente/estilo, sprites repetidos o marcadores de mapas.​
- Cuando puedes identificar claramente el estado intrínseco a compartir y pasar el estado extrínseco desde el contexto en cada operación del objeto.​

### Notas y diferencias

- Flyweight no es Singleton: puede haber muchas instancias, pero una por cada combinación de estado intrínseco; la fábrica decide cuándo reutilizar o crear nuevas.​
- Se integra bien con Factory para gestionar el pool y con Composite cuando los nodos comparten características repetidas pero se posicionan distinto en la estructura.​

## Proxy

### Propósito

Proxy es un patrón de diseño estructural que te permite proporcionar un sustituto o marcador de posición para otro objeto. Un proxy controla el acceso al objeto original, permitiéndote hacer algo antes o después de que la solicitud llegue al objeto original.

### Cuándo usarlo

- El proxy implementa LectorArchivo y administra la vida del objeto real, aplicando inicialización diferida y almacenamiento en caché sin que el cliente cambie su forma de uso; ambos son intercambiables por la misma interfaz.​

- Este patrón también se usa para proxies remotos (invocaciones a servicios externos), protección (chequear permisos antes de delegar) o contadores/limitares de uso, manteniendo transparente el acceso para el cliente.​

### Diferencias rápidas

A diferencia de Decorator, cuyo objetivo es añadir responsabilidades, Proxy se centra en controlar el acceso manteniendo la misma interfaz, y suele gestionar el ciclo de vida del servicio real; Facade ofrece una interfaz nueva y simplificada a un subsistema, no sustituye al objeto original.
