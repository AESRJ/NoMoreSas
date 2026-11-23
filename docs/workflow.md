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

## Snapshots de tareas revisadas y cadencia de commits

El helper `scripts/release_review_commit.py` acepta revisiones locales con paths explicitos. `--prepare` congela un unico indice; `--wait` puede esperar en un proceso oculto hasta los veinte minutos desde el commit anterior. La base y el tree se vuelven a comprobar antes del commit; si cambiaron, se aborta y Codex revisa, sin resetear ni falsificar fechas.

Una revision puede incluir `reviewed_blobs`, un mapa exacto de cada path a `{oid, mode}`. Codex guarda esos blobs de Git al aceptar la tarea, despues de verificarla. Asi el helper puede preparar mas tarde el contenido aceptado aunque el archivo de trabajo haya avanzado con otra tarea autorizada. Primero valida todos los objetos y modos, luego prepara solo esos paths; no restaura ni modifica el working tree. No permite secretos, bases locales, `.local` ni rutas fuera del checkout. Las secciones de historia se seleccionan de forma explicita para conservar cambios previos ajenos al commit.

Antes de preparar el siguiente snapshot, Codex confirma el commit anterior y revisa la nueva base. Sigue habiendo un solo indice congelado. Los blobs no permiten saltar la revision, mezclar tareas, reducir la cadencia ni afirmar commits futuros. Verificacion del cambio de arnes: fixture Git aislado con objeto invalido rechazado antes de indexar, contenido aceptado preservado y working tree posterior intacto; `py_compile` correcto.
