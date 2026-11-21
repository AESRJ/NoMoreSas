# Implementation Plan: Catálogo público y comparación

**Branch**: directorio independiente de rama; trabajar en `feat/catalogo-comparacion` al construir. **Date**: 2026-11-20. **Spec**: [spec.md](spec.md).

**Input**: Especificación del catálogo; frontend y Express confirmados explícitamente por el usuario. Fuente de decisiones: [ADR 0002](../../docs/decisions/0002-stack-y-primer-incremento.md).

## Summary

Construir una SPA React con React Router declarativo y Zustand para seleccionar hasta tres alternativas. Express sirve un catálogo curado versionado mediante una API JSON de lectura. Se priorizan búsqueda, fichas y comparación, con estados accesibles de carga, vacío, error y recurso inexistente. Claude Code implementa; Codex revisa.

## Technical Context

**Language/Version**: JavaScript moderno con ES Modules; Node.js LTS 26.13.1 instalado. No exigir TypeScript: no fue solicitado para clase.

**Primary Dependencies**: React, React DOM, React Router, Zustand, Express 5, Vite, Helmet; Vitest, React Testing Library, Supertest, Playwright y ESLint para comprobar el incremento. pnpm 12.21.0 instalado; fijar `packageManager` a `pnpm@12.21.0`. Claude resolverá versiones compatibles verificando `engines` y peers, fijará dependencias directas exactas y versionará `pnpm-lock.yaml`. No usar generadores remotos sin versión fija ni introducir Next.js/NestJS.

**Storage**: `apps/api/data/catalog.json` versionado, validado al iniciar. Sin escrituras públicas, base de datos ni cuentas. La selección de comparación vive en memoria de la SPA, no en el backend.

**Testing**: Vitest para API, lógica de selección y UI; Supertest para API sin abrir puertos; Testing Library para comportamiento; Playwright para recorrido con API real y recarga de rutas. Se solicitan expresamente estas pruebas para demostrar FR-012.

**Target Platform**: desarrollo local Windows; navegador moderno de escritorio y móvil. API en `127.0.0.1:3001`, web en `127.0.0.1:5173`, ambos configurables; sin despliegue externo.

**Project Type**: monorepo pnpm con `apps/web` y `apps/api`, sin un paquete compartido hasta que exista una necesidad real.

**Performance Goals**: no se introduce una promesa de carga concurrente ni latencia sin medición. Para el catálogo inicial basta un fetch al entrar y búsqueda/filtros locales; la interfaz debe responder sin consultar servicios externos.

**Constraints**: respetar React/React Router/Zustand/pnpm/Express, español, teclado, vistas 360/1280 px, datos trazables y alcance sin ejecución remota.

**Scale/Scope**: mínimo tres SaaS y cuatro alternativas verificadas; catálogo, listado por SaaS, ficha y comparación. Selección de cero a tres alternativas; mínimo dos para comparar.

## Constitution Check

| Principio | Antes de investigación | Después del diseño |
| --- | --- | --- |
| Especificación antes de construir | Spec completa y checklist verificado | Contratos, modelo, tareas y entrega requeridos |
| Codex planifica; Claude construye | Confirmado | Ningún código de producto escrito por Codex |
| Fuentes y control de datos | Curación explícita, sin datos personales | No se publican hechos sin fuente ni cifras de ejemplo como garantías |
| Cambios acotados | Un incremento público de lectura | Sin SSH, cuentas, despliegue ni base de datos prematura |
| Evidencia y memoria | Informes y Git previstos | Pruebas y pasos de memoria definidos |

Resultado de diseño: sin violaciones. El cierre requiere revisar resultados reales, no basta este plan.

## Project Structure

### Documentation (this feature)

`spec.md`, `plan.md`, `research.md`, `data-model.md`, `contracts/http-api.md`, `contracts/ui.md`, `catalog-sources.md`, `quickstart.md`, `checklists/requirements.md`, `tasks.md`.

### Source Code (repository root)

```text
package.json
pnpm-workspace.yaml
pnpm-lock.yaml
eslint.config.js
playwright.config.js
apps/
  api/
    package.json
    data/catalog.json
    src/app.js
    src/server.js
    src/catalog.js
    src/errors.js
    tests/catalog.test.js
    tests/api.test.js
  web/
    package.json
    index.html
    vite.config.js
    src/main.jsx
    src/App.jsx
    src/api/catalog.js
    src/hooks/useCatalog.js
    src/store/comparison.js
    src/components/
    src/pages/
    src/styles.css
    tests/
tests/e2e/catalog.spec.js
```

Las rutas son propuestas para Claude, no archivos existentes. Se preservan `scripts/`, los tests Python del arnés y las reglas de agentes. Las pruebas JavaScript no sustituyen esas comprobaciones.

## Architecture and execution

- Express separa la aplicación de `listen`; carga y valida el dataset al arrancar. Si es inválido, el servidor termina con error claro en vez de servir datos parciales. Se prueban la validación y las rutas con fixtures.
- `GET /api/catalog` entrega una instantánea completa y pequeña. La búsqueda por nombre de SaaS o alternativa ocurre en el cliente sobre esa instantánea; no se duplican algoritmos de búsqueda en API y cliente.
- `GET /api/alternatives/:id` permite el contrato de ficha; la UI reutiliza la instantánea cuando ya la tiene. IDs se validan antes de buscar.
- Vite hace proxy de `/api` a la API local. No habilitar CORS global; no se necesita cuando la web utiliza ese proxy. El despliegue futuro requerirá otro diseño de hosting, no es parte de esta entrega.
- React Router en modo declarativo: `/`, `/saas/:id`, `/alternativas/:id`, `/comparar` y ruta desconocida. El estado de carga/error pertenece a la obtención del catálogo; búsqueda en URL `q`, selección en Zustand. Al recargar se pierde la selección por diseño y `/comparar` informa cómo elegir opciones.
- No ejecutar fetch en cada pulsación ni almacenar una segunda copia del catálogo en Zustand. El módulo de carga comparte caché por sesión entre rutas; ofrece reintento y evita que respuestas obsoletas sobrescriban datos recientes. No añadir librería de datos remotos en este incremento.
- React muestra contenido como texto; prohibido `dangerouslySetInnerHTML` para datos de catálogo. Enlaces oficiales solo HTTP(S) y enlace externo seguro. API con Helmet, identificación desactivada y errores sin stack al cliente.
- Zustand implementa únicamente IDs ordenados, añadir con resultado de éxito/límite, retirar y limpiar. La validación con datos cargados elimina IDs retirados con aviso visible.

## Commands to implement

Los comandos todavía NO existen: Claude debe definirlos en T001 y T013.

- `pnpm dev`: web y API en paralelo; sin publicación de red externa.
- `pnpm lint`: ESLint para código JS/JSX de apps, pruebas y configuración propia; no recorrer archivos generados de Spec Kit.
- `pnpm test`: pruebas unitarias/UI/API sin navegador externo.
- `pnpm build`: compilación de la SPA.
- `pnpm test:e2e`: Playwright con web/API reales, inicia y cierra ambos procesos mediante `webServer`.
- `pnpm exec playwright install chromium`: prerrequisito de la verificación de navegador; no confundir falta de navegador con fallo funcional.

## Complexity Tracking

No hay excepciones a la constitución. Se descartan ORM, microservicios, autenticación, SSR y persistencia de selección entre sesiones en esta fase. El archivo JSON no se utilizará como persistencia concurrente de usuarios/proyectos.
