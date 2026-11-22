# Tasks: Flujo final004
Fuente spec.md/plan.md; ejecución/checks solo en .project/ del checkout de código. Una tarea por invocación Claude; Codex revisa y commitea. Sin autoaprobación ni push.

## Phase 1: Setup
Entorno ya instalado. Verificar init.cmd/entrega004 antes de T001; no reinstalar stack.
## Phase 2: Foundational
Contratos de003 disponibles. Migración aditiva se incluye en T002, sin escritores simultáneos.

## Phase 3: US1 — Catálogo vigente
Meta independiente: cinco fichas/fuentes y comparación, referencias antiguas conservadas.
- [ ] T001 [US1] Actualizar apps/api/data/catalog.json, apps/api/src/catalog.js y etiquetas de licencia en apps/web/src; cinco alternativas/servicios de research.md, retirar GitHub/Gitea/Forgejo, no borrar proyectos históricos. Sustituir cobertura antigua del seed sin relaciones inventadas, corregir fixtures afectados. FR001/SC001. Verificar tests enfocados catálogo y lectura de referencia retirada.

## Phase 4: US2 — Perfil y evaluación
Meta independiente: guardar equipo privado y recibir evaluación honesta.
- [ ] T002 [US2] Crear migración aditiva en apps/api y persistencia/endpoints privados de contracts/workflow.md, con validación completa de data-model.md: Profile.projectId, Profile.cpuCores, Profile.ramGiB, Profile.storageGiB, Profile.os, Profile.architecture, Profile.storageKind, Profile.users, Profile.dataGiB, Profile.access, Profile.hasDomain, Profile.cpuFeaturesKnown, Profile.revision. GETworkflow sin perfil y PUTprofile; ownership/CSRF/parser existentes. Durante esta tarea evaluation/plan null y progress vacío hastaT003/T004, no cambiar forma final. FR002/010. Verificar perfil inválido, dos usuarios, persistencia y migración idempotente con DB temporal.
- [ ] T003 [US2] Implementar reglas/datos versionados y evaluación en apps/api/src y apps/api/data según data-model.md Evaluation.status, Evaluation.rulesVersion, Evaluation.items, Evaluation.totals, Evaluation.warnings; ecuación/carga/margen explícitos, fuentes fechadas y referencias oficiales separadas. Requisitos por plataforma y desconocidos/retirados, sin garantías. Integrar GET/PUTworkflow. FR003/004, SC004. Verificar insuficiente/desconocido y cálculo reproducible con tests enfocados.

## Phase 5: US3 — Plan y progreso
Meta independiente: API de plan/prompt y progreso persistente lista para UI.
- [ ] T004 [US3] Implementar plantillas, etapas y progreso privado en apps/api/src con data-model.md Plan.fingerprint, Plan.steps, Plan.blocked, Progress.projectId, Progress.fingerprint, Progress.completedStepIds, Progress.updatedAt. Todas las cinco alternativas, instrucciones nativas WireGuard y fuentes/versiones, sin claves/SSH/ejecución/IAexterna. Hash incluye selección/perfil/reglas/templates,409obsoleto y borrado en cascada, transacción evita carrera. FR005/006/007, SC003. Verificar regeneración, copytexto con contexto, aislamiento y reinicio DB temporal.
- [ ] T005 [US2] [US3] Implementar recorrido completo apps/web/src (API/store/rutas/componentes): /proyectos/:id/flujo Equipo/Evaluación/Plan enlazado desde proyecto, todos los campos Profile deT002, reglas/avisos deT003, prompts y checkboxes persistidos deT004. Mantener separación de usuario/abort stale, errores/reintentos/recarga y fallback clipboard; advertir antes de cambiar configuración con progreso. FR002–008/010, SC002/003/004. Verificar happy path real y error/401 con comprobaciones enfocadas, sin mocks que oculten integración.

## Phase 6: US4 — Presentación
Meta independiente: todas las vistas coherentes en móvil y escritorio.
- [ ] T006 [US4] Aplicar paleta exacta de spec FR009 a apps/web/src y computadora focal central en portada. Invocar Impeccable, sin generar PRODUCT.md/DESIGN.md ni documentar su mejora. Intentar asset con Higgsfield MCP registrado; si aprobación/OAuth impide generarlo, reportar dependencia y seguir UI, sin sustituir origen ni afirmar tarea completa de imagen. Sitio minimalista atractivo y profesional, estados privados/públicos coherentes, navegación funcional. SC005. Revisar360/1280 y teclado.

## Phase 7: Polish & cross-cutting
- [ ] T007 Ejecutar verificaciones esenciales de quickstart.md y corregir regresiones dentro del alcance; añadir smoke del recorrido en tests/e2e con DB temporal y privacidad API. Ajustar CI/fixtures de catálogo afectados sin eliminar pruebas de seguridad ni fingir ejecuciones. Actualizar README.md, .project/context.md, .project/verification.md y .project/progress/impl_MVP-CIERRE.md con arranque, comandos/resultados reales y pendientes. FR008/010, SC001–005. Codex realiza revisión independiente y cierre, nunca Claude.

## Dependencies & execution strategy
T001→T002→T003→T004→T005→T006→T007. US1 independiente de persistencia nueva; US2API trasT003, US3API trasT004, recorrido completoT005. Solo un escritor: no paralelizar archivos ni iniciar tareas futuras en una invocación. La imagen puede seguir pendiente externamente sin frenar API/UI. Priorizar entrega rápida revisable; no ampliar funciones ni repetir suites completas por tarea.

## Parallel opportunities
Solo investigación/lectura de fuentes independientes de código. No escritores paralelos; revisión Codex entre tareas. Los ejemplos de validación por historia están en quickstart.md.
