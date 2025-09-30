### Monorepositorios: Guía completa con prácticas y ejemplos

Este documento explica con detalle qué es un monorepositorio, cuándo conviene adoptarlo, en qué se diferencia de un monolito o un polyrepo, cuáles son las capacidades esenciales de las herramientas modernas, y cómo empezar con ejemplos prácticos. La guía se basa en el contenido de `monorepo.tools` y experiencia práctica adicional.

—

### ¿Qué es un monorepositorio?

Un monorepositorio (monorepo) es un único repositorio que contiene múltiples proyectos distintos con relaciones bien definidas entre ellos. No es solo “colocación de código”: la clave son las relaciones explícitas, la modularidad y la gestión de dependencias interna.

- Monorepo ≠ Monolito
  - Un monolito suele ser una sola aplicación grande sin encapsulación clara. Un buen monorepo, en cambio, promueve modularidad y límites bien definidos entre proyectos.
- Monorepo ≠ “un repo gigante sin orden”
  - La estructura, las reglas de dependencia y la orquestación de tareas son esenciales para que escale.

Referencia: [Understanding Monorepos — monorepo.tools](https://monorepo.tools/#understanding-monorepos)

—

### ¿Por qué un monorepo?

- Compromisos atómicos entre proyectos
  - Los cambios que afectan a múltiples librerías y aplicaciones se aplican en un solo commit, evitando rupturas por versionado cruzado.
- Una sola versión de todo
  - Evita incompatibilidades por múltiples versiones de dependencias compartidas.
- Menos fricción para compartir código
  - Reutilización sin publicar paquetes externos para consumidores internos.
- Movilidad de desarrolladores y tooling consistente
  - Estándares únicos para build, test, lint, deploy, facilitando contribuciones cruzadas.

Comparado con polyrepos, reduce:
- Duplicación de código y esfuerzos.
- Coste de cambios coordinados en múltiples repos.
- Inconsistencias de herramientas y pipelines.

Referencia: [Why a Monorepo — monorepo.tools](https://monorepo.tools/#why-a-monorepo)

—

### Capacidades clave que deben aportar las herramientas

Según `monorepo.tools`, para que un monorepo escale, el tooling debe cubrir:

- Caché de cómputo local y distribuido
  - Evita recompilar/retestear lo mismo. La variante distribuida comparte artefactos entre máquinas/CI.
- Orquestación de tareas
  - Ejecutar en el orden correcto y en paralelo, respetando dependencias.
- Detección de proyectos afectados
  - Ejecutar solo lo que cambió basándose en el grafo de dependencias y el diff.
- Ejecución remota transparente y distribuida
  - Escalar builds y tests a workers remotos cuando el tamaño crece.
- Análisis del workspace y visualización del grafo
  - Entender dependencias y limitar acoplamientos.
- Estandarización de tooling y generación de código
  - Un set consistente de comandos, con scaffolding cuando sea útil.

Herramientas destacadas (no exhaustivo): Bazel, Gradle Build Tool, Lage, Lerna, moon, Nx, Pants, Rush, Turborepo. Cada una ofrece distintas combinaciones de estas capacidades.

Referencia: [Monorepo features — monorepo.tools](https://monorepo.tools/#monorepo-features)

—

### Ejemplo 1: Monorepo TypeScript con workspaces

Estructura básica con `pnpm`/`npm` workspaces:

```text
repo/
  package.json
  tsconfig.base.json
  packages/
    ui-components/
      package.json
      src/
    utils-formatting/
      package.json
      src/
  apps/
    web-app/
      package.json
      src/
    api-service/
      package.json
      src/
```

`package.json` (raíz) con workspaces:

```json
{
  "name": "org-monorepo",
  "private": true,
  "workspaces": ["packages/*", "apps/*"],
  "scripts": {
    "build": "turbo run build",
    "test": "turbo run test",
    "lint": "turbo run lint"
  },
  "devDependencies": {
    "turbo": "^2.0.0"
  }
}
```

Ejemplo de dependencias internas:

```json
// apps/web-app/package.json
{
  "name": "web-app",
  "dependencies": {
    "ui-components": "*",
    "utils-formatting": "*"
  }
}
```

Con Turborepo/Nx, se cachean builds/tests por paquete, se paraleliza y se ejecuta solo lo afectado.

—

### Ejemplo 2: Grafo de dependencias y “affected”

Supón que cambias `utils-formatting`. El sistema calcula qué depende de él y ejecuta tareas solo para esos paquetes:

```bash
# Nx
nx graph | cat
nx affected:test --base=origin/main --head=HEAD | cat

# Turborepo (concepto similar con filtros)
turbo run test --filter=...utils-formatting | cat
```

Esto mantiene el feedback rápido incluso con docenas de apps y paquetes.

—

### Ejemplo 3: Reglas de dependencia y límites

Define políticas para evitar acoplamientos indebidos:

- Un paquete de `packages/` no puede depender de `apps/`.
- Ciertas capas solo importan desde capas inferiores (p. ej., `domain` no importa `infra`).
- Usa etiquetas/“scopes” y validadores (Nx “tagging”, ESLint rules, Bazel visibility) para reforzar estas reglas.

Beneficios: evita “spaghetti deps”, facilita refactors y reduce deuda técnica.

—

### Prácticas recomendadas

- Delimitar módulos y contratos
  - Interfaces claras entre librerías; publicar APIs mínimas.
- Estándares de proyecto
  - Scripts y pipelines coherentes; plantillas para nuevos paquetes/apps.
- CI inteligente
  - Ejecutar solo afectados, cachear resultados, paralelizar.
- Observabilidad del repo
  - Grafo visible, métricas de tiempos de build/test.
- Reglas de dependencia
  - Visibilidad/tagging para preservar arquitectura.
- Gestión de versiones internas
  - Preferir una sola versión por dependencia compartida.

—

### Riesgos y cómo mitigarlos

- Build/test lentos al crecer
  - Caché distribuido, ejecución remota, pipelines por “affected”.
- Complejidad inicial de tooling
  - Empezar simple (workspaces + orquestador), evolucionar a capacidades avanzadas cuando escale.
- Falta de límites claros
  - Definir dominios, carpetas, reglas y validación automática.
- Cuellos de botella en CI
  - Paralelismo, sharding de tareas y escalamiento horizontal.

—

### ¿Cuándo elegir monorepo, polyrepo o híbrido?

- Monorepo
  - Muchas piezas que evolucionan juntas, alto reuso, equipos que colaboran frecuentemente.
- Polyrepo
  - Componentes altamente independientes, contratos estables, ciclos de vida muy distintos.
- Híbrido
  - Monorepos por dominios o plataformas, con algunos repos aislados para componentes muy específicos.

—

### Pasos para empezar (receta mínima)

1) Organiza carpetas por apps y paquetes compartidos.
2) Habilita workspaces (`npm`, `pnpm` o `yarn`).
3) Elige un orquestador (Nx o Turborepo) con caché local; agrega caché remoto después.
4) Define reglas de dependencia y etiquetado por capas/domínios.
5) Configura CI para “affected” y paralelismo.
6) Visualiza el grafo y monitorea tiempos.
7) Escala con ejecución distribuida/remota si es necesario.

—

### Referencias

- `monorepo.tools` — Understanding Monorepos: [https://monorepo.tools/#understanding-monorepos](https://monorepo.tools/#understanding-monorepos)


