# App Cafetería Digital

Útii para explicar Estilos de Arquitectónicos, Patrones Arquitectónicos y Patrones de Diseño

## 1. El Patrón de Diseño: Factory (El "Zoom" al Código) 🧱

Dónde mirar: **Archivo logica_cafe.py.**

- **La explicación:** "Miren la clase FabricaDeCafe. ¿Ven que el resto del sistema no sabe cómo se hace un café? Solo le dicen 'dame un latte' y ella lo construye. Eso es un Patrón de Diseño".

- **Por qué es de "Diseño":** Porque resuelve un problema de objetos y clases. Si mañana quiero cambiar la receta del Espresso, solo cambio una línea de código en este archivo. Es una solución táctica, local y de bajo nivel.

Enlaces de interés: [Enlace](https://refactoring.guru/es/design-patterns)


## 2. El Patrón Arquitectónico: Capas (El "Zoom" a las Carpetas) 🏢

**Dónde verlo:** El explorador de archivos (la estructura de carpetas).

- **La explicación:** "Noten que tenemos tres archivos separados. El HTML no sabe nada de Python, y el archivo logica_cafe.py no sabe nada de rutas web. Hemos dividido el software en Capas".

1. **Capa de Presentación:** index.html (lo que el usuario ve).
2. **Capa de Control:** app.py (el que recibe los pedidos).
3. **Capa de Negocio:** logica_cafe.py (el que sabe las reglas del café).

Por qué es "Arquitectónico": Porque define el esqueleto de nuestra aplicación. Si mezcláramos todo en un solo archivo de 1,000 líneas, el "edificio" se caería al intentar ampliarlo.

## 3. El Estilo Arquitectónico: Cliente-Servidor (El "Zoom" Global) 🌍

**Dónde mirar:** La terminal de VSC (donde dice 127.0.0.1:5000) y el navegador.

- **La explicación:** "Aquí hay dos programas hablando por un cable invisible (HTTP). El navegador (Cliente) está en un lugar y mi servidor Flask (Servidor) está en otro. El cliente pide y el servidor sirve".

- **Por qué es un "Estilo":** Porque es la filosofía global. No importa si el servidor está en Python o Java, o si el cliente es un celular o una PC; las reglas de comunicación (petición/respuesta) son las mismas para todo el ecosistema. Es el nivel más alto de abstracción.

