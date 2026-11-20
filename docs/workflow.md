# Operación diaria con SDD

## Sesión de Codex

1. Leer `AGENTS.md`, `progress/current.md`, contexto y constitución. Ejecutar `init.ps1`.
2. Tomar una funcionalidad del backlog. En el chat de Codex: `$speckit-specify <necesidad>`; después `$speckit-clarify` si hay dudas. Respetar la numeración generada en `specs/`.
3. Ejecutar `$speckit-plan <restricciones técnicas acordadas>`, `$speckit-tasks` y `$speckit-analyze` sobre la misma funcionalidad. Registrar `SPECIFY_FEATURE` cuando los scripts lo necesiten; no depender del nombre de rama.
4. Resolver huecos y fijar criterios y comandos reales. Crear entrega JSON desde `handoffs/template.json`. El autor es `codex`, el ejecutor `claude-code`; poner `ready` únicamente cuando no falten decisiones necesarias.
5. Actualizar estado y backlog; una funcionalidad activa como máximo. Abrir una rama de trabajo si ya existe un commit inicial. Nunca ejecutar `$speckit-implement` en Codex.

## Sesión de Claude Code

1. Leer `CLAUDE.md` y la entrega. En PowerShell, por ejemplo: `$env:SPECIFY_FEATURE = '002-nombre'`. Ese valor corresponde a la carpeta real generada.
2. Ejecutar `.\.venv\Scripts\python.exe scripts/check_harness.py --implementation-ready handoffs/<entrega>.json`.
3. En el chat de Claude: `/speckit-implement Implementa únicamente las tareas de la entrega indicada`. Activar los especialistas necesarios; un escritor por archivo.
4. Ejecutar las verificaciones del plan, actualizar checkboxes y registrar salida resumida con comandos y códigos de salida en `progress/impl_<feature>.md`.
5. Solicitar revisión de Codex. No cerrar ni autoaprobar el resultado.

## Revisión y memoria

Codex compara spec, plan, tareas, diff y evidencia. Registra hallazgos con severidad y criterio afectado. Si hay correcciones, Claude las implementa. Codex puede usar `$speckit-converge` para evaluar y añadir tareas, manteniendo la construcción en Claude. Una vez cumplidos los checkpoints, Codex actualiza el índice a `done` y cierra la entrega. Ambos actualizan contexto e historial; el responsable de la sesión registra si NotebookLM se sincronizó.

El flujo oficial proporciona skills de implementación también a Codex y de planificación a Claude. Su presencia no cambia los permisos acordados en este proyecto. No modificar esos archivos generados para imponer los roles: las reglas viven en `AGENTS.md`, `CLAUDE.md` y la constitución.
