# Instrucciones del repositorio

## Responsabilidades

- El usuario dirige producto y prioridades.
- **Codex siempre planifica y revisa. Claude Code construye la aplicación.** Codex puede editar especificaciones, planes, tareas, decisiones, documentación y memoria; no implementar ni reparar código de producto, ni ejecutar `speckit-implement`.
- El montaje inicial del arnés, sus verificadores y configuración está autorizado expresamente en esta sesión. Esa excepción no autoriza construir la aplicación con Codex.
- Claude implementa solamente una entrega `ready` de Codex. No cambia el alcance ni se autoaprueba. Si falta una decisión, informa el bloqueo con evidencia y devuelve el punto a Codex.
- Los roles y prompts orientan a los agentes; no son un aislamiento de seguridad entre procesos.

## Al empezar y al cerrar

1. Leer `progress/current.md`, `docs/context/project-context.md` y `feature_list.json`.
2. Leer `.specify/memory/constitution.md`; después, solo los documentos y fuentes relevantes para la tarea.
3. Ejecutar `.\init.ps1`. Distinguir fallos del arnés de herramientas externas pendientes.
4. Consultar NotebookLM si está autenticado y aporta contexto; verificar las citas contra las fuentes. Si falla, continuar con Git e indicar la limitación.
5. Actualizar `progress/current.md`, registrar resultados y comandos en `progress/history.md` sin borrar entradas previas. No guardar razonamiento interno, cookies ni secretos.

## Flujo SDD

`specify → clarify → plan → tasks → analyze → handoff → implement → review/converge`.
Codex usa `$speckit-specify`, `$speckit-clarify`, `$speckit-plan`, `$speckit-tasks`, `$speckit-analyze`; Claude usa `/speckit-implement`. Los skills de planificación instalados en Claude no cambian esta distribución. `converge` en Codex solo evalúa y documenta trabajo pendiente; toda corrección vuelve a Claude.

- Una funcionalidad `in_progress` como máximo. Un único escritor por archivo.
- `specs/<NNN-nombre>/spec.md`, `plan.md` y `tasks.md` son la fuente de trabajo; `feature_list.json` es su índice.
- No promover borradores a entregas listas sin criterios observables, alcance, dependencias y comandos de verificación definidos.
- No inventar requisitos, valores de hardware, resultados de pruebas ni conexiones MCP.
- Cambios de arquitectura requieren una decisión en `docs/decisions/`.
- No ejecutar despliegues, SSH, compras o cambios de servidores como parte del MVP.

## Git y trazabilidad

Commits en español, pequeños y descriptivos; explicar qué, por qué y cómo se verificó. Usar la identidad real del usuario configurada en Git; no inventar datos ni añadir coautoría automática. Documentar la asistencia de agentes en la bitácora. No publicar con `push` salvo instrucción explícita. No versionar credenciales. Ver `CHECKPOINTS.md` y `docs/conventions.md`.

## Documentación por demanda

- Producto y preguntas: `docs/product/`.
- Roles y delegación: `docs/agents.md`.
- Operación SDD y entregas: `docs/workflow.md`, `handoffs/README.md`.
- Memoria: `docs/notebooklm.md`, `docs/context/`.
- Validación: `docs/verification.md`.
