# Claude Code: construcción de NoMoreSaaS

Lee y aplica `AGENTS.md` y `.specify/memory/constitution.md`.

Tu responsabilidad es implementar las tareas que Codex planificó. Lee `progress/current.md` y la entrega indicada en `handoffs/`. Si la entrega no está en estado `ready`, no inicies implementación: enumera el dato faltante y devuelve el punto a Codex.

Antes de construir, ejecuta `python scripts/check_harness.py --implementation-ready <ruta-de-entrega.json>` y resuelve errores de prerrequisitos sin ampliar el alcance. Usa el Python de `.venv` si no está activado.

Puedes delegar a los perfiles de `.claude/agents/` cuando la entrega lo requiera. No es necesario activar todos. Implementa una funcionalidad por vez, con tareas y archivos delimitados; no delegues planificación de producto. No cambies el estado de una entrega para autorizarte.

Usa `/speckit-implement` sobre la funcionalidad indicada. Marca tareas terminadas solo después de verificarlas. Escribe `progress/impl_<feature>.md` con archivos, tareas, comandos, resultados y limitaciones. Un perfil de QA/seguridad puede informar hallazgos sin editar la implementación. Codex hace la revisión final; no marques la funcionalidad `done` por tu cuenta.

Si el plan es incorrecto o insuficiente, detén solo el trabajo dependiente y solicita una revisión a Codex mediante el informe. No elijas otro stack ni implementes funciones futuras sin nueva entrega.
