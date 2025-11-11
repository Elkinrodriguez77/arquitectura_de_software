# Patrones de Comportamiento — Guía

Esta guía resume qué problema resuelve cada patrón, cuándo usarlo y cómo reconocer su estructura en código.

## Tabla comparativa

| Patrón                  | Problema que resuelve                                                          | Idea central (1 frase)                                                                   | Cuándo usarlo                                                            | Señales en el código                                                 |
| ----------------------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------- |
| Chain of Responsibility | Evitar if/else encadenados para validar/procesar solicitudes en etapas         | Pasar la solicitud por una cadena; cada manejador decide procesar o delegar al siguiente | Validaciones por pasos, filtros, autorización multinivel                 | Clases “Handler” con método handle y referencia al siguiente eslabón |
| Command                 | Desacoplar “quién pide” de “quién ejecuta” y permitir deshacer/rehacer o colas | Convertir cada acción en un objeto con ejecutar() y deshacer()                           | Editores con undo/redo, colas de trabajos, macro-comandos                | Clases de comando, invocador que guarda historial                    |
| Iterator                | Recorrer una colección sin exponer su representación interna                   | Proveer un iterador uniforme para secuencias heterogéneas                                | Estructuras propias (árboles, grafos) que se quieren recorrer fácilmente | Implementar **iter** o un objeto iterador separado                   |
| Mediator                | Reducir dependencias entre múltiples objetos que se comunican                  | Centralizar la interacción en un mediador que orquesta mensajes                          | Chats, formularios con campos interdependientes, widgets UI              | Clase “Mediator” y colegas que llaman al mediador, no entre sí       |
| Memento                 | Guardar/restaurar estado sin violar encapsulamiento                            | Tomar “snapshots” opacos y restaurarlos más tarde                                        | Deshacer, checkpoints, guardar borradores                                | Métodos crear_memento() y restaurar(memento) en el originador        |
| Observer                | Notificar a muchos interesados cuando algo cambia                              | Suscripción: el sujeto emite eventos, observadores reaccionan                            | UIs reactivas, buses de eventos, cache invalidation                      | Subject con suscribir()/notificar(); Observers con update()          |
| State                   | Evitar condicionales por estado; comportamiento cambia con el estado           | Encapsular estados como objetos; el contexto delega en el estado actual                  | Máquinas de estados, reproductores, workflows                            | Estados con misma interfaz; contexto que cambia de estado            |
| Strategy                | Elegir algoritmos intercambiables en runtime                                   | Inyectar una estrategia con la misma interfaz                                            | Cálculo de costos, políticas de pricing, rutas                           | Clases “Estrategia” con un método común; cliente acepta cualquiera   |
| Template Method         | Fijar un proceso y permitir variar pasos específicos                           | La superclase define el esqueleto; subclases implementan pasos                           | Pipelines de reportes, parsers, ETL simples                              | Método generar() que llama a pasos abstractos                        |
| Visitor                 | Añadir operaciones a una jerarquía estable sin modificarla                     | Doble despacho: elemento.aceptar(visitor) llama visitor.visitX                           | Árboles/ASTs, estructuras donde cambian las operaciones                  | Interfaz Visitor con visit_X; elementos con aceptar(visitor)         |

## Notas pedagógicas

- Primero se debe validar el problema y luego el patrón: si se reconoce el dolor (ifs largos, acoplamiento, duplicación), se entenderá por qué el patrón ayuda.
- Los patrones son vocabulario compartido y plantillas que se adaptan al contexto, no reglas rígidas; úsalos cuando simplifiquen el diseño, no antes.
- Ubica los patrones por intención: creacionales crean objetos, estructurales ensamblan componentes, y de comportamiento coordinan responsabilidades y algoritmos.

## Glosario esencial

- Sujeto/Observador: publicador y suscriptores que reaccionan a eventos (Observer).
- Estrategia: algoritmo intercambiable que comparte una interfaz (Strategy).
- Memento: objeto opaco que guarda estado interno para restaurarlo luego (Memento).
- Mediador: punto central que reduce conexiones en malla entre objetos (Mediator).
- Comando: acción convertida en objeto con ejecutar/deshacer (Command).
- Estado: variaciones de comportamiento modeladas como objetos estado (State).
- Iterador: forma estándar de recorrer colecciones sin exponer su estructura (Iterator).
- Plantilla: esqueleto de proceso con pasos redefinibles (Template Method).
- Visitante: operación externa que recorre una jerarquía estable (Visitor).
