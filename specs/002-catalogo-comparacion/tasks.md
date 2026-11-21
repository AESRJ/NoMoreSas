# Tasks: Catálogo público y comparación

**Input**: `specs/002-catalogo-comparacion/`. Leer spec, plan, research, modelo, contratos, guía de fuentes y quickstart.

**Prerequisites**: entrega `ready` de Codex y puerta del arnés correcta. Tecnologías confirmadas: React, React Router, Zustand, pnpm y Express. Vite/JavaScript son elecciones de planificación documentadas.

**Tests**: Solicitados expresamente en FR-012. Crear los casos de cada historia y comprobar que detectan el comportamiento ausente antes de implementar; después verificar que pasan. No marcar una tarea completa por escribir código sin comprobarlo.

**Organization**: una funcionalidad activa, entregada incrementalmente US1 → US2 → US3. Todas las tareas de implementación pertenecen a Claude Code; Codex revisa después.

## Phase 1: Setup

- [ ] T001 Crear `package.json`, `pnpm-workspace.yaml`, `pnpm-lock.yaml`, `apps/web/package.json`, `apps/api/package.json`, `apps/web/index.html`, `apps/web/vite.config.js`, `eslint.config.js` y `.env.example`; usar React con Vite y JavaScript, React Router declarativo, Zustand y Express 5, dependencias directas exactas compatibles con Node 26.13.1, `packageManager: pnpm@12.21.0`, scripts lint/test/build/dev de `plan.md` y proxy `/api` sin CORS abierto; actualizar `.gitignore` solo para artefactos de aplicación e incluir `apps/web/src/main.jsx` y `apps/web/src/App.jsx` como shell inicial (FR-009, FR-011, FR-012).

## Phase 2: Foundational

- [ ] T002 Implementar carga inmutable y validación del catálogo en `apps/api/src/catalog.js`, con pruebas que detecten fixtures inválidos en `apps/api/tests/catalog.test.js`, conforme a `data-model.md`: `Service.id`, `Service.name`, `Service.description`; `Alternative.id`, `Alternative.name`, `Alternative.description`, `Alternative.capabilities`, `Alternative.limitations`, `Alternative.license` incluyendo label/url/classification, `Alternative.difficulty` incluyendo level/explanation, `Alternative.hostingNotes`, `Alternative.officialUrl`, `Alternative.documentationUrl`, `Alternative.sources`; `Relation.serviceId`, `Relation.alternativeId`, `Relation.coverage`; `Source.url`, `Source.checkedAt`, `Source.supports`, `Source.kind`, `Source.note`. Aplicar exactamente las restricciones de cada campo y las reglas de conjunto, sin ejecutar contenido ni aceptar escrituras públicas (FR-003, FR-004, FR-006, FR-011).
- [ ] T003 Curar `apps/api/data/catalog.json` usando `catalog-sources.md`: comprobar fuentes oficiales vigentes, licencias, fechas reales y motivos editoriales; cubrir tres SaaS, cuatro alternativas y dos relacionadas con un mismo SaaS. Aplicar los campos y fuentes de `data-model.md` implementados en T002; registrar enlaces y fecha de comprobación efectiva en `progress/impl_MVP-CATALOGO.md`; no dar las URLs candidatas por verificadas sin visitarlas (FR-002, FR-003, FR-004, FR-010).
- [ ] T004 Implementar `apps/api/src/app.js`, `apps/api/src/server.js`, `apps/api/src/errors.js` y pruebas HTTP en `apps/api/tests/api.test.js`: endpoints, orden estable, validación de ID, errores 400/404/500 sin stacks, headers, ausencia de escrituras, salud y fallo de arranque con dataset inválido según `contracts/http-api.md`; separar app de listen y enlazar por defecto solo `127.0.0.1:3001` (FR-001, FR-003, FR-008, FR-011, FR-012).
- [ ] T005 [P] Implementar el store en `apps/web/src/store/comparison.js` y pruebas en `apps/web/tests/comparison.test.js` de acuerdo con `data-model.md`, campo `ComparisonSelection.ids`: 0–3 IDs únicos ordenados, añadir duplicado/cuarto sin mutar incorrectamente, retirar, limpiar y reconciliar IDs retirados con aviso; no persistir entre recargas (FR-005, FR-007).
- [ ] T006 Implementar `apps/web/src/api/catalog.js`, `apps/web/src/hooks/useCatalog.js` y pruebas de carga compartida en `apps/web/tests/catalog-client.test.js`: instantánea compartida por sesión, reintento, cancelación/respuestas obsoletas y diferenciación error/vacío; no duplicar catálogo en Zustand ni consultar por pulsación; preparar componentes comunes en `apps/web/src/components/` según `contracts/ui.md` (FR-001, FR-008, FR-009).

**Checkpoint**: API y cliente comparten contrato; seed validado, store y carga comprobados. T005 puede avanzar tras T001 en archivos propios; T003 y T004 requieren T002 y la integración completa requiere el seed.

## Phase 3: User Story 1 - Descubrimiento (P1)

**Goal**: navegar y buscar alternativas sin cuenta. **Independent Test**: búsqueda existente, normalizada, vacía y sin coincidencias; catálogo vacío y error con reintento.

- [ ] T007 [US1] Escribir casos de aceptación UI en `apps/web/tests/catalog.test.jsx` y fixtures propios: catálogo inicial, nombre de SaaS/alternativa, normalización, q vacío, URL compartible, sin coincidencias, error con reintento, catálogo vacío y enlaces por SaaS; comprobar que fallan antes de T008 (FR-001, FR-002, FR-008, FR-009).
- [ ] T008 [US1] Implementar `apps/web/src/pages/CatalogPage.jsx`, `apps/web/src/pages/ServicePage.jsx` y componentes de tarjetas/búsqueda en `apps/web/src/components/`; integrar rutas `/` y `/saas/:id` en `apps/web/src/App.jsx`, búsqueda q en URL y criterios de `contracts/ui.md`, nombre accesible, foco visible y estados recuperables; hacer pasar T007 (FR-001, FR-002, FR-008, FR-009).

## Phase 4: User Story 2 - Fichas verificables (P2)

**Goal**: comprender capacidades y límites con fuentes. **Independent Test**: ficha directa válida, desconocida y datos no verificados.

- [ ] T009 [P] [US2] Escribir pruebas en `apps/web/tests/detail.test.jsx` para ficha por enlace/directa, licencia, dificultad editorial, capacidades, limitaciones, notas, fuentes/fecha y datos desconocidos; contenido del catálogo no debe ejecutarse como HTML; comprobar fallo antes de T010 (FR-003, FR-004, FR-008, FR-009).
- [ ] T010 [US2] Implementar `apps/web/src/pages/AlternativePage.jsx`, `apps/web/src/pages/NotFoundPage.jsx`, componentes de fuentes/dificultad y rutas `/alternativas/:id` y wildcard en `apps/web/src/App.jsx`; resolver desde instantánea compartida, enlaces HTTP(S) seguros, sin HTML crudo, navegación de vuelta y comportamiento de `contracts/ui.md`; hacer pasar T009 (FR-003, FR-004, FR-008, FR-009).

## Phase 5: User Story 3 - Comparación (P3)

**Goal**: comparar de dos a tres opciones y conservar selección al navegar. **Independent Test**: límites, duplicados, quitar/limpiar, navegación y necesidades diferentes.

- [ ] T011 [P] [US3] Escribir pruebas en `apps/web/tests/compare.test.jsx` para selección 0/1/2/3/4, duplicados, quitar/limpiar, persistencia durante navegación, aviso por IDs retirados y comparación de necesidades distintas; comprobar fallo antes de T012 (FR-005, FR-006, FR-007, FR-008, FR-009).
- [ ] T012 [US3] Implementar `apps/web/src/pages/ComparePage.jsx`, controles de selección/conteo en `apps/web/src/components/` y ruta `/comparar` en `apps/web/src/App.jsx`; integrar tarjetas/ficha mediante componentes comunes, mostrar criterios alineados, desconocidos explícitos, aviso de necesidades distintas y tabla utilizable en pantalla estrecha; hacer pasar T011 sin romper US1/US2 (FR-005, FR-006, FR-007, FR-009).

## Phase 6: Polish and cross-cutting verification

- [ ] T013 Implementar `playwright.config.js`, `tests/e2e/catalog.spec.js` y script raíz `test:e2e` con API y web reales: recorrido buscar/ficha/selección/comparación, URL directa y recarga de ficha, pérdida deliberada de selección al recargar comparación, teclado y vistas 360/1280; mock de fallos solo en pruebas, sin alterar seed. Registrar diferencias entre cobertura automatizada y revisión visual; ejecutar lint/test/build/e2e y conservar evidencia (FR-001–FR-012, SC-001–SC-005).
- [ ] T014 Ajustar `apps/web/src/styles.css` y componentes existentes para español, foco, etiquetas, avisos accesibles, carga/error/vacío y comparación estrecha; revisar con teclado y navegador a 360/1280 y registrar capturas/observaciones en `progress/impl_MVP-CATALOGO.md`; no declarar auditoría WCAG completa (FR-008, FR-009, SC-004).
- [ ] T015 [P] Añadir `.github/workflows/catalog.yml` con Node compatible y pnpm 12.21.0, instalación frozen-lockfile, lint, pruebas, build y e2e; preservar `.github/workflows/harness.yml` y tests Python. Actualizar `README.md` y `docs/verification.md` con comandos ejecutables reales, prerrequisitos y límites, sin prometer funciones futuras (FR-010, FR-011, FR-012).
- [ ] T016 Revisar seguridad del incremento y registrar hallazgos en `progress/security_MVP-CATALOGO.md`: catálogo como texto, enlaces permitidos, entradas de ID, errores sin stack, API sin escrituras y sin exposición externa. Corregir hallazgos de implementación dentro del alcance y repetir verificaciones afectadas; este informe no sustituye la revisión final de Codex (FR-004, FR-008, FR-011, FR-012).
- [ ] T017 Completar `progress/impl_MVP-CATALOGO.md`, actualizar `progress/current.md`, añadir entrada a `progress/history.md` y actualizar `docs/context/project-context.md` con tareas/archivos/comandos y códigos de salida reales, límites, estado de memoria y siguiente paso; ejecutar `init.cmd` y pedir revisión de Codex sin marcar la feature done ni cambiar la autorización de la entrega (FR-012 y constitución V).

## Dependencies and execution order

T001 → T002 → T003/T004 → T006 → US1 → US2 → US3 → verificación final. T005 es independiente tras T001 y se integra antes de US3. El orden T007→T008, T009→T010 y T011→T012 mantiene verificación antes de construcción de cada historia. T013 exige las tres historias; T014–T017 cierran la integración. No desplegar.

## Parallel opportunities

- T005 puede delegarse al implementador de estado mientras backend avanza T002–T004: archivos distintos.
- T009 y T011 pueden preparar sus archivos de prueba con fixtures después de la base, pero T010/T012 respetan el orden de integración y un único escritor en `App.jsx`.
- T015 puede escribir el workflow tras estabilizar los scripts y contratos de ejecución; coordinar cambios de README con T017.
- Solo una persona/agente edita cada archivo. Frontend/backend/QA/seguridad se usan según necesidad; no lanzar todos por defecto.

## Coverage and acceptance

| Requisito | Tareas principales |
| --- | --- |
| FR-001 | T004, T006, T007, T008, T013 |
| FR-002 | T003, T007, T008 |
| FR-003 | T002, T003, T004, T009, T010 |
| FR-004 | T002, T003, T009, T010, T016 |
| FR-005 | T005, T011, T012 |
| FR-006 | T002, T011, T012 |
| FR-007 | T005, T011, T012, T013 |
| FR-008 | T004, T006–T014, T016 |
| FR-009 | T007–T014 |
| FR-010 | T003, T013, T015 |
| FR-011 | T001, T002, T004, T015, T016 |
| FR-012 | T001, T004, T007, T009, T011, T013–T017 |
| SC-001 | T003, T007, T008, T013 |
| SC-002 | T002, T003, T009, T010 |
| SC-003 | T005, T011, T012, T013 |
| SC-004 | T013, T014 |
| SC-005 | T007, T009, T011, T013, T017 |

## Implementation strategy

Demostrar primero US1 sobre la base validada, después fichas y comparación. No ejecutar manuales completos de instalación de Nextcloud ni otros servicios: se están describiendo alternativas, no desplegándolas. Si una dependencia no se puede resolver, informar a Codex con evidencia sin reemplazar tecnologías confirmadas. Cerrar tareas con evidencia; Codex revisa spec/plan/diff/resultados antes de cerrar la funcionalidad.
