# Tasks: Equipo asistido y prompts claros con seguridad
Snapshot de planificación: ejecución/checkboxes SOLO .project/specs/007-equipo-y-plan-seguro/tasks.md del código. Una tarea porinvocaciónClaude; Codex revisa y hacecommit. No autoaprobar.

## Phase1 Setup
Entorno/stack existente, no reinstalar ni cambiar componentes globales. Ejecutarinit/entrega y leer spec/plan/modelo/contrato antes de tarea.
## Phase2 Foundational
Dependencias: UX-REVISION code reviewed, AUTH-GOOGLE migration003 code reviewed. Un escritorporarchivo, no construcción de siguiente tarea en misma invocación.
## Phase3 Historias y entregas
Meta: las historias de spec.md y criterios observables de quickstart.md.
- [ ] T001 [US2] Construir recopiladorWindows Node22+ descargable y guía de uso en apps/web/public/downloads (o fuente propia tools/diagnostic compilada apublic), sololecturasistema/CIMfijo timeout y únicoJSONdeexportflagwx. data-model.md Diagnostic.schemaVersion, Diagnostic.capturedAt, Diagnostic.os, Diagnostic.architecture, Diagnostic.cpu, Diagnostic.ramBytes, Diagnostic.volumes, Diagnostic.gpuNames. Noejecutar inventario real ni capturaridentificadores del desarrollador; usarfixtures y pruebas deconsultasfijas. FR003/008.

- [ ] T002 [US1] Implementar esquema/validación/importpreview y ayuda parcialbrowser en apps/web/src y validación/persistenciaprovenance en apps/api con migración004aditiva. data-model.md el modelo Diagnostic completo y ProfileProvenance.projectId, ProfileProvenance.target, ProfileProvenance.fields, ProfileProvenance.collectorVersion; normalizar unidades y validar enamboslados. Selecciónvolumen/equipodestino, guardar explícito/manualconservado. FR001/002/004/005. Verificarinvalid/oversize/unknown/rangos/owner y perfilesanteriores.

- [ ] T003 [US3] Aclarar WorkflowPage/EvaluationView y reglascerteza enAPI; data-model.md ProfileProvenance.fields, ProfileProvenance.target, Profile.revision (contrato existente ../004-flujo-final/data-model.md). Aproximacionesetiquetadas/pendientes, resúmenesCPU/RAM/disco y detalle desplegable, siguienteacciónclara. Manual/import nocausandatosfalsos, cambios invalidanavance. FR005/006. Verificar3estados y persistencia/recalculado.

- [ ] T004 [US3] Revisar plan-templates/plan y UI de prompts de las5alternativas con bloques claros de seguridad/validación/recuperación pertinentes a etapa; actualizarversionesreglas/templates e invalidación004. FR007/008. Guía y evidencia .project/progress/impl_MVP-EQUIPO-ASISTIDO.md; lint/build, prueba representativa import/manual/plan/privacidad y navegador360/1280. NoSSH/ejecución ni pruebas redundantes.

## Phase4 Polish y cierre
Laúltima tarea incluyeintegración/checks/evidencia; Codex cierra sólo tras verificación, sin nuevos cambios de producto por Codex.
## Dependencies / strategy
T001 → T002 → T003 → T004. MVP primero porhistoria; no marcar próximas porinferencia. Paralelismo sololectura/investigación, nunca escritoresmismosarchivos. Bibliotecas/versiones/fuentes se verifican alinstalar. Condicionesexternaspendientes no seocultan.
