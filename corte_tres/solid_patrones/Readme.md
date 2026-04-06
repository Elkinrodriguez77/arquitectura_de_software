# SOLID

## Principio S - Responsabilidad Única:

### 1. Crear carpeta "principio_s":

**Razón de este principio:** Una clase debe tener una sola razón para cambiar.

1. Creamos un archivo restaurante_sin_patron.py
2. Creamos un archivo restaurante_con_patron.py:

Para resolver esto aplicamos SRP (Responsabilidad Única) separando los roles, y lo combinamos con el **Patrón Facade (Fachada)**.

El patrón Facade nos dice: "Crea una fachada simple (el Restaurante) que oculte la complejidad de los subsistemas (Chef, Cajero, Inventario)"


## Principio 🔓 O - Abierto/Cerrado (OCP) + Patrón Strategy

El principio Abierto/Cerrado (Open/Closed Principle) nos dice: "Las entidades de software deben estar abiertas para su extensión, pero cerradas para su modificación".

Suena a contradicción, ¿verdad? Volvamos a tu respuesta anterior. Dijiste: "Modifico solo Cajero". Si agregamos PayPal y luego Criptomonedas modificando el Cajero directamente, nuestro código se vería así:

```python
class Cajero:
    def procesar_pago(self, monto, metodo):
        if metodo == "tarjeta":
            print(f"💳 Cobrando ${monto} con tarjeta")
        elif metodo == "paypal":
            print(f"📱 Cobrando ${monto} con PayPal")
        # Si mañana hay otro método, tenemos que volver a abrir y modificar esta clase...
```

El problema aquí es que cada vez que agregamos un método, tenemos que "abrir" el código existente, arriesgándonos a dañar lo que ya funciona.

Para solucionar esto sin tocar el Cajero, usamos el **Patrón Strategy (Estrategia)**. Este patrón nos permite definir una familia de algoritmos (métodos de pago), encapsular cada uno y hacerlos intercambiables.

## Principio 🔄 L - Sustitución de Liskov (LSP) + Patrón Factory

El principio de Sustitución de Liskov dice que si tienes una clase padre (como MetodoPago), debes poder reemplazarla por cualquiera de sus clases hijas (PagoTarjeta, PagoPayPal) sin que el programa se rompa o se comporte de forma extraña.

Como ya aseguramos que todas las hijas tienen el método pagar(monto) gracias a nuestra interfaz, cumplimos Liskov perfectamente. El cajero confía a ciegas.

Pero ahora surge un problema práctico en la vida real: **¿Cómo decide el sistema qué objeto crear si el cliente selecciona el método de pago en una pantalla?**

Si llenamos nuestro código principal de if y else para crear los pagos, volvemos a ensuciar la arquitectura. Aquí es donde entra el **Patrón Factory (Fábrica).**

Una "Fábrica" es una clase que tiene una sola misión: encargarse de la lógica de creación de objetos para que las demás clases no tengan que hacerlo.

## principio I - Segregación de Interfaces (ISP) + Patrón Adapter (Adaptador).

El problema de las interfaces gigantes (ISP): Imaginemos que tenemos una interfaz general Trabajador que obliga a usar los métodos trabajar() y comer(). Si el restaurante compra un RobotLimpiador, este sabe trabajar(), pero no necesita comer(). La solución es dividir esa interfaz en dos más pequeñas para que el robot solo adopte las funciones que realmente usa.

Integrando sistemas externos (Patrón Adapter): Ahora, supongamos que adquirimos otro robot de una marca externa. Su código es cerrado y en lugar de la función estándar trabajar(), trae una llamada iniciar_bateria_y_limpiar(). Como no podemos modificar su código, aplicamos el Patrón Adapter. Creamos una clase intermedia que "traduce" nuestro estándar a la instrucción que el robot entiende. Es literalmente como ponerle un adaptador a un enchufe extranjero para que funcione en nuestra toma de corriente.

## Principio D 🏗️ Llegamos a la D - Inversión de Dependencias (DIP)

La regla de DIP dice: "Los módulos de alto nivel (el Restaurante) no deben depender de los módulos de bajo nivel (los empleados concretos). Ambos deben depender de abstracciones (interfaces)".

Para lograr esto en la práctica, usamos una técnica llamada Inyección de Dependencias 💉: en lugar de que el restaurante construya a sus empleados "por dentro" (self.cocinero = CocineroHumano()), se los vamos a "inyectar" (pasar) desde afuera a través de los parámetros del __init__.

Para que sea una Inyección de Dependencias real y cumpla DIP, el Restaurante debe exigir interfaces y no clases concretas.
