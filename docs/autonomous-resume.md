# Recuperacion del 22-11-2026 a las18:28

La tarea original inicio14:21 y el coordinador fallo15:45. El usuario renovo trabajo. Codex confirmo commits y recupero T002Google; ClaudeT003 devolvio limite5h hasta19:20 con trabajo parcial conservado. La nueva tareaWindows NoMoreSaaS-Reanudar-20261122-1921 esta registrada y verificada Ready para19:21 America/Tijuana. No hay garantia de cuota o equipo disponible.

El arnes valida la entrega activa configurada (ahora006), HEAD, indice y archivos conservados. Lee nota de recuperacion antes de continuar; no repite005 cerrada. Los errores futuros se clasifican sin persistir mensajes sensibles. Consultar.local/release-resume-state.json y reporte; cuota o fallo externo no equivale a trabajo en progreso. Cancelacion enabled=false en.local/release-resume-config.json.

## Configuracion anterior (historica)

# Reanudación y commits por tarea

La cola de ejecución vive en `.project/execution-queue.json` del checkout de código. Solo005 está activa y ready. Codex puede activar las siguientes entregas planificadas después de revisar dependencias; Claude no se autoautoriza.

La reanudación local utiliza Codex CLI como coordinador independiente y Claude Code como constructor. Codex no implementa producto ni Docker. Hay una tarea de Claude por invocación y revisión explícita antes del commit. El helper exige veinte minutos entre commits; no falsea fechas ni crea commits vacíos.

El inicio está registrado para el 22-11-2026 a las 14:21, America/Tijuana, un minuto después del último aviso de restablecimiento de Claude. **El horario no garantiza cuota disponible.** A las 13:42 se verificó la tarea Windows `NoMoreSaaS-Reanudar-20261122-1421`, estado Ready y próxima ejecución a las 14:21. Registro en `.local/release-schedule-registration.json`; configuración y preparación del código en `.local/release-resume-config.json`.

## Condiciones

- Equipo encendido y sesión del usuario disponible. La tarea permite iniciar al volver a estar disponible, no enciende el ordenador por su cuenta.
- Autenticación local de Codex y Claude vigente; no cambiar cuentas o modelos para esquivar límites.
- Rama, HEAD, índice y cambios preexistentes iguales a la preparación. Si alguien modifica producto antes del inicio, se detiene para preservar ese trabajo.
- No dos coordinadores escribiendo a la vez; lock por proceso y tarea de Windows sin instancias superpuestas.
- La publicación final requiere configuración Google y acceso/costo de Railway verificados. Una conexión declarada, un build o un callback simulado no equivalen a despliegue terminado.

## Consultar y cancelar

- Estado: `.local/release-resume-state.json` en el maestro.
- Reporte del coordinador: `.local/release-coordinator-report.md`.
- Metadatos de ejecución: `.local/release-coordinator-events.jsonl`; no guarda razonamiento ni salidas crudas de herramientas.
- Evidencia y tareas de producto: `.project/progress/` y `.project/specs/` del código.
- Para cancelar antes de iniciar, cambiar `enabled` a `false` en el archivo de configuración local y desactivar la tarea del programador. Si está ejecutándose, el controlador revisa esa bandera y detiene únicamente su propio árbol de procesos. Pedir «pausa» permite a Codex realizar esa cancelación.

Los scripts de arnés están en `scripts/resume_release.py`, `resume-release.ps1`, `invoke_claude_release_task.ps1` y `release_review_commit.py`. El último solo acepta manifiestos de revisión creados por Codex; los roles son instrucciones de operación, no un aislamiento de seguridad entre procesos.
