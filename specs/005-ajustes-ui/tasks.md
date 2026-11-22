# Tasks: Exploración por servicio y revisión de interfaz
Snapshot de planificación: ejecución/checkboxes SOLO .project/specs/005-ajustes-ui/tasks.md del código. Una tarea porinvocaciónClaude; Codex revisa y hacecommit. No autoaprobar.

## Phase1 Setup
Entorno/stack existente, no reinstalar ni cambiar componentes globales. Ejecutarinit/entrega y leer spec/plan/modelo/contrato antes de tarea.
## Phase2 Foundational
Dependencias: 004 cerrado. Un escritorporarchivo, no construcción de siguiente tarea en misma invocación.
## Phase3 Historias y entregas
Meta: las historias de spec.md y criterios observables de quickstart.md.
- [ ] T001 [US1] Actualizar SearchForm/CatalogPage y copy de AuthForm/AuthPage bajo apps/web/src; label/placeholder/ayuda/título/bajada segúnplan. Referencias ExplorerState.query de data-model.md; password sin modificar15–128/Unicode/hash. Adaptar nombres accesibles y textos en pruebas existentes. FR001/006. Verificar lint y tests catálogo/hero/auth afectados, sin nueva batería espejo.

- [ ] T002 [US2] Conservar data-model.md Service.id, data-model.md Service.name, data-model.md Service.description y construir explorador circular/árbol/comparativa integrada en apps/web/src y retirar interfaz global de comparación; conservar ficha y redirección interna /comparar. Metadatos oficiales deService y validación opcional en apps/api/data/catalog.json y src/catalog.js según data-model.md Service.officialUrl, Service.sources; estado según ExplorerState.activeServiceId, ExplorerState.activeAlternativeId, ExplorerState.query. Curar fuentes sin paridad/precios inventados. FR002/003/004/007. Verificar selección/cambio/teclado/reducedmotion y rutas antiguas con smoke enfocado.

- [ ] T003 [US3] Implementar ServiceReplacementPicker y usarlo en ProjectFormPage para crear/editar por servicio conocido, chips/quitar y retiradas. data-model.md ProjectSelection.alternativeIds; persistencia003 intacta. FR005. Verificar dos servicios, duplicados/quitar, edición/reintento/401 y aislamiento existente.

- [ ] T004 [US4] Integrar y corregir regresiones005 dentro de alcance; actualizar pruebas viejas del recorrido global obsoleto conservando intención de búsqueda/selección/privacidad. README/contexto/evidencia breves .project/progress/impl_UX-REVISION.md. FR001–007/SC001–003. Lint/build, tests afectados y smoke navegador360/1280; Codex revisa/cierra, no Claude. Ajuste Codex2026-11-22: estabilizar únicamente fixtures de apps/api/tests/db.test.js para la prueba de cuota100 que agota5s bajo carga; conservar aserciones/semántica/aislamiento y verificar pnpm test integrado, sin cambiar configuraciónDB ni límites de producto.

## Phase4 Polish y cierre
Laúltima tarea incluyeintegración/checks/evidencia; Codex cierra sólo tras verificación, sin nuevos cambios de producto por Codex.
## Dependencies / strategy
T001 → T002 → T003 → T004. MVP primero porhistoria; no marcar próximas porinferencia. Paralelismo sololectura/investigación, nunca escritoresmismosarchivos. Bibliotecas/versiones/fuentes se verifican alinstalar. Condicionesexternaspendientes no seocultan.
