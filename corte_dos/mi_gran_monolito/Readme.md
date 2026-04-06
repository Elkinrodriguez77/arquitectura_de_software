1. Instalar entorno virtual
2. Instalar flask -- pip install flask


Pedir:

curl -X POST http://127.0.0.1:5000/pedir -H "Content-Type: application/json" -d "{\"id\": 1}"

curl -X POST http://127.0.0.1:5001/pedir -H "Content-Type: application/json" -d "{\"id\": 1}"


# Comparativa de Arquitecturas: Del Monolito a los Microservicios

| Característica | Monolito (Carpeta 01) | Monolito Modular (Carpeta 02) | Microservicios (Carpeta 03) |
| :--- | :--- | :--- | :--- |
| **Unidad de Despliegue** | Un solo archivo/proceso único. | Un proceso único (código organizado). | Múltiples procesos independientes. |
| **Comunicación** | Llamadas directas a funciones. | Llamadas entre clases y métodos. | Llamadas por red (HTTP/REST). |
| **Acoplamiento** | **Muy Alto:** Todo depende de todo. | **Medio:** Lógica separada, memoria compartida. | **Bajo:** Totalmente independientes. |
| **Aislamiento de Fallos** | **Nulo:** Un bug tumba toda la app. | **Bajo:** Un error crítico detiene el proceso. | **Alto:** Un servicio cae, el otro sigue vivo. |
| **Escalabilidad** | Escalar todo o nada. | Escalar todo o nada. | Escalabilidad granular por servicio. |
| **Base de Datos** | Una sola DB para todo el código. | Una sola DB para todo el código. | **Database per Service** (Datos aislados). |
| **Complejidad** | Baja (Fácil de desarrollar). | Media (Fácil de mantener). | Alta (Requiere gestión de red/puertos). |