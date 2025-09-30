### Arquitectura de Software: Guía viva para estudiantes

Esta guía está diseñada como un espacio de aprendizaje teórico–práctico en constante evolución. Parte desde el rol y responsabilidades del arquitecto/a de software y avanza hacia prácticas modernas, herramientas, metodologías y el uso de IA (incl. NotebookLM) para potenciar el trabajo arquitectónico. Usaremos diferentes caso, como el proyecto RG‑T4185 del Banco Interamericano de Desarrollo (BID) sobre la Factura Electrónica de Comercio Exterior (FE‑X) para aprender haciendo.

—

### ¿Qué implica ser Arquitecto/a de Software?

Un/a arquitecto/a de software es responsable de traducir objetivos de negocio en decisiones técnicas sostenibles, priorizando atributos de calidad (rendimiento, seguridad, disponibilidad, mantenibilidad, observabilidad), alineando equipos y mitigando riesgos técnicos mediante decisiones explícitas y documentadas.

- Responsabilidades clave
  - Entender profundamente el problema y el contexto organizacional.
  - Elicitar y priorizar requisitos funcionales y atributos de calidad (QAS) usando marcos como ISO/IEC 25010.
  - Diseñar la arquitectura conceptual y lógica (p. ej., modelos C4) y seleccionar estilos (microservicios, event‑driven, modular monolith, SOA, serverless, data mesh, etc.).
  - Definir integración, contratos y esquemas (API first, eventos, mensajería, estándares del dominio).
  - Incorporar seguridad por diseño (amenazas, cifrado, IAM, firma/PKI), gobernanza de datos y cumplimiento (privacidad, regulatorios, trazabilidad).
  - Diseñar para el cambio: versionado, evolución, compatibilidad, migración.
  - Establecer prácticas de observabilidad (logs, métricas, trazas), resiliencia (circuit breakers, timeouts), fiabilidad (SLO/SLA), y automatización (CI/CD, IaC).
  - Gestionar decisiones con ADRs, evaluar trade‑offs (ATAM/CBAM) y reducir deuda técnica.
  - Facilitar comunicación: diagramas, documentación ligera (arc42), talleres con stakeholders.

- Artefactos típicos
  - Vision statement y mapa de objetivos vs. capacidades.
  - Catálogo de stakeholders y mapa de procesos.
  - Requisitos/QAS priorizados con escenarios medibles.
  - Vista C4 (Contexto, Contenedores, Componentes, Código) y diagramas complementarios (UML cuando aporta valor).
  - ADRs (Architectural Decision Records) con motivación y alternativas evaluadas.
  - Modelos de amenazas y controles.
  - Especificaciones de APIs/eventos y políticas de versionado.
  - Roadmap de evolución y plan de transición/migración.

- Herramientas recomendadas
  - Modelado y documentación: C4, arc42, PlantUML, Structurizr, draw.io/diagrams.net (en este curso usaremos también `Recursos/Metodologia-Desarrollo de soluciones.drawio.png`).
  - Gestión de decisiones: ADRs (Markdown + repositorio Git).
  - Evaluación: ATAM, QAS, lightweight fitness functions.
  - Entrega: Git, CI/CD, contenedores, IaC (Terraform), plataformas cloud.
  - Observabilidad: OpenTelemetry, Prometheus, Grafana.
  - Seguridad: threat modeling (STRIDE), PKI, secretos gestionados, escaneo SCA/SAST/DAST.
  - IA de apoyo: NotebookLM para estudio de documentos, LLMs con RAG para sintetizar requisitos, copilotos para acelerar análisis y documentación.

—

### IA como acelerador del rol arquitectónico

La IA no sustituye el criterio arquitectónico, pero multiplica su alcance:

- Análisis asistido de fuentes extensas (términos de referencia, REOI, planes de adquisiciones) con NotebookLM.
- Generación de primeros borradores de QAS, ADRs y diagramas descriptivos a partir de contexto curado por el/la arquitecto/a.
- Identificación de lagunas, riesgos y supuestos implícitos para guiar talleres con stakeholders.
- Trazabilidad: mapeo entre objetivos, requisitos, decisiones y controles.

Buenas prácticas: proporcionar a la IA fuentes confiables, desambiguar términos del dominio, pedir evidencias y citas, y validar cada resultado con juicio experto.

—

### Tabla de contenidos del curso

| Módulo | Título | Objetivos principales | Entregables | Lecturas/Recursos |
| --- | --- | --- | --- | --- |
| 0 | Contexto: rol del Arquitecto/a de Datos y Software | Diferenciar ámbitos, responsabilidades y puntos de intersección | Glosario, mapa de stakeholders | ISO/IEC 25010, guías BID |
| 1 | Entender el problema (caso BID RG‑T4185) | Contextualizar FE‑X, identificar objetivos, restricciones y actores | Problem Statement, C4 Context, primeros ADRs | Página del proyecto BID, REOI |
| 2 | Elicitación de requisitos y atributos de calidad | Definir RF y QAS con criterios medibles | Catálogo RF/QAS priorizado | ATAM/QAS, ejemplos |
| 3 | Arquitectura conceptual (C4 Ctx/Contenedores) | Esbozar límites, capacidades y flujos | Diagramas C4 nivel 1‑2 | C4 Model |
| 4 | Estilos y patrones | Elegir estilos: microservicios, EDA, modular monolith, etc. | ADR selección de estilo | Catálogos de patrones |
| 5 | Integración y datos | APIs, eventos, contratos, data governance | Especificaciones API/eventos | Estándares dominio |
| 6 | Seguridad y cumplimiento | Modelo de amenazas, PKI, firma, privacidad | Modelo STRIDE + controles | Normativas aplicables |
| 7 | Nube y plataforma | Plataforma, IaC, CI/CD, multiregión | Diagrama plataforma, pipeline | Guías cloud |
| 8 | Observabilidad y resiliencia | SLOs, trazas, métricas, caos | Plano de observabilidad | OTel, SRE |
| 9 | Gestión de decisiones | ADRs, debt register, fitness functions | ADRs revisados | arc42, ADR templates |
| 10 | IA aplicada a arquitectura | NotebookLM, RAG, copilotos | Notebook/Playbook IA | Guías de prompting |
| 11 | Evaluación de arquitectura | ATAM/CBAM y trade‑offs | Informe de evaluación | ATAM |
| 12 | Roadmap y transición | Plan por etapas y riesgos | Roadmap, hitos, riesgos | Gestión del cambio |

—

### Contexto del rol: Arquitecto/a de Datos

Antes de profundizar en software, necesitamos una base de datos sólida:

- Gobierno y calidad de datos: linaje, catalogación, MDM, privacidad y cumplimiento.
- Arquitecturas de datos: data lakehouse, data mesh, CDC/ELT, streaming.
- Modelado y contratos de datos: esquemas versionados, evolución y compatibilidad.
- Integridad y trazabilidad para escenarios regulados como FE‑X (firma digital, validación, auditoría, retención).
- Interoperabilidad internacional: estándares (p. ej., WCO Data Model, UN/CEFACT, UBL, e‑Invoicing), semántica y mapeos.

—

### Módulo 1 (Clave): Entender el problema con el caso RG‑T4185 (BID)

Usaremos el proyecto del BID “Apoyo a la gestión digital fiscal y aduanera en América Latina y el Caribe” como caso guía. Sí, es este caso: RG‑T4185, con foco en la Factura Electrónica de Comercio Exterior (FE‑X), buscando digitalización, trazabilidad e integridad del comercio, y eficiencia en la recaudación.

web: https://www.iadb.org/es/proyecto/RG-T4185

- Datos principales del proyecto (según BID)
  - Número de proyecto: RG‑T4185. Etapa: Implementación.
  - Aprobación: 30 nov 2022. Cooperación Técnica, sector Ciencia y Tecnología.
  - Objetivo: implementación armonizada de FE‑X entre países de ALC, de modo que el valor del comprobante de exportación se convierta en el valor de la declaración de importación en el país receptor.
  - Operación: ATN/OC‑19713‑RG (No reembolsable, USD).

- Problema y oportunidad
  - Interoperabilidad transfronteriza de comprobantes electrónicos, con requisitos de integridad, autenticidad, disponibilidad y trazabilidad.
  - Armonización normativa y técnica entre administraciones tributarias y aduaneras.
  - Eficiencia operativa para empresas y mejora de cumplimiento fiscal.

- Actores y stakeholders iniciales
  - Administraciones tributarias y aduaneras de países ALC.
  - Exportadores, importadores, operadores logísticos, cámaras de comercio.
  - Proveedores tecnológicos, certificadoras, y plataformas de intercambio.
  - Organismos multilaterales de apoyo y gobernanza.

- Supuestos y restricciones típicas (a validar)
  - Cumplimiento de estándares regionales/internacionales y marcos legales vigentes.
  - Infraestructura de firma digital/PKI, timestamping, y validación.
  - Protección de datos y acuerdos de intercambio transfronterizo.
  - Continuidad operativa, ventanas de mantenimiento y recuperación ante desastres.

- Entregables del módulo
  - Problem Statement con objetivos, métricas y riesgos.
  - Diagrama C4 Nivel Contexto, actores y flujos principales.
  - Primeros ADRs (p. ej., estilo arquitectónico, estrategia de interoperabilidad, enfoque de firma/validación).
  - Catálogo inicial de QAS con escenarios medibles (p. ej., “Validación de comprobante transfronterizo en <2s P95, 99.9% disponibilidad”).

—

### Guía práctica: Analizar el REOI con NotebookLM e IA

Fuente local clave: `Recursos/RG-T4185-P001 - Paquete REOI.pdf` (resumen de la licitación). Complementar con documentos del BID (Documento de CT, Plan de Adquisiciones y publicaciones relacionadas).

Pasos sugeridos
1) Preparar las fuentes
   - Subir a NotebookLM: el REOI local y enlaces oficiales del proyecto.
   - Agregar glosario de dominio (FE‑X, aduanas, WCO, UBL, PKI) como notas.
2) Contextualizar con prompts
   - “Resume objetivos, alcance y restricciones regulatorias del proyecto RG‑T4185. Cita las secciones.”
   - “Extrae stakeholders, roles y dependencias institucionales. Lista supuestos explícitos e implícitos.”
3) Extraer requisitos y QAS
   - “Diferencia requisitos funcionales vs. atributos de calidad. Para cada QAS, formula un escenario medible (estímulo–respuesta–métrica).”
4) Riesgos y vacíos de información
   - “Identifica riesgos técnicos, normativos y operativos. Propón preguntas para talleres.”
5) Primeros artefactos
   - “Propon un diagrama C4 nivel Contexto (texto estructurado). Sugiere ADRs iniciales con alternativas y trade‑offs.”
6) Verificación cruzada
   - Pedir a la IA que cite fuentes exactas. Validar manualmente contra los documentos.
7) Curación y versión
   - Consolidar en Markdown en el repositorio (ADRs, QAS, contexto). Versionar cambios y decisiones.

—

### Temas siguientes y roadmap de la asignatura

- Arquitectura conceptual y estilos
  - Modular monolith vs microservicios; event‑driven; orquestación/coreografía; CQRS/ES.
  - Contratos y evolución de esquemas (APIs, eventos, JSON/Avro/Protobuf, UBL).

- Integración y datos en el contexto FE‑X
  - Interoperabilidad entre administraciones; mapeos al WCO Data Model; validación y reconciliación.
  - PKI, firmas digitales, sellos de tiempo, OCSP/CRL; almacenes de claves y HSMs.

- Seguridad, cumplimiento y gobierno
  - Modelado de amenazas (STRIDE), privacidad transfronteriza, DLP, auditoría.
  - Controles: cifrado en tránsito/descanso, segregación de ambientes, gestión de secretos.

- Plataformas y entrega
  - CI/CD, IaC, entornos multi‑región, tolerancia a fallos, SLOs.
  - Observabilidad con OpenTelemetry; caos engineering ligero.

- Evaluación y decisiones
  - ATAM/CBAM, fitness functions, tech debt management.
  - ADRs como mecanismo de trazabilidad.

- IA aplicada al ciclo arquitectónico
  - NotebookLM y RAG para análisis de documentos regulatorios.
  - Copilotos para documentación, generación de escenarios de prueba y análisis de cobertura de riesgos.

—

### Referencias

- Proyecto BID RG‑T4185 (Apoyo a la gestión digital fiscal y aduanera en ALC): [Página del proyecto](https://www.iadb.org/es/proyecto/RG-T4185)
- Documentos relacionados (según BID):
  - REOI: [RG-T4185-P001 - Paquete REOI.pdf](https://www.iadb.org/document.cfm?id=EZIDB0000474-1089185423-3)
  - Documento de CT: [Documento de CT.pdf](https://www.iadb.org/document.cfm?id=EZSHARE-505838969-26)
  - Términos de Referencia: [Terminos de Referencia.pdf](https://www.iadb.org/document.cfm?id=EZSHARE-505838969-24)
  - Plan de Adquisiciones: [Plan de Adquisiciones_62973.pdf](https://www.iadb.org/document.cfm?id=EZSHARE-505838969-25)


