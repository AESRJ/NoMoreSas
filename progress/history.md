# Bitácora (añadir entradas; no reescribir sesiones previas)

## 2026-11-19 — Montaje inicial — Codex

Solicitud: arnés similar a Betta Tech, SDD con GitHub Spec Kit, Codex planificador, Claude constructor, memoria NotebookLM y documentación paso a paso.

Hallazgos: repositorio sin commits; remoto `AESRJ/NoMoreSas`; PDF local de 13 páginas. Cuenta GitHub autenticada consultada: Israel Gomez Ahumada (`issgg`, ID 198836279), sin email público. No había identidad Git configurada. Usar nombre verificado y correo noreply de esa cuenta para el commit inicial, sin modificar identidad global.

Acciones: entorno `.venv`; herramientas fijadas; `specify init` para Codex e `integration install claude`; constitución y roles adaptados; síntesis de producto con referencias por página; backlog y borrador de descubrimiento; configuración MCP y scripts de operación. Los archivos oficiales de Spec Kit se conservan sin reescribir sus skills.

NotebookLM: `nlm login --check` informó que no existe el perfil `default`. No se creó ni se cargó ningún cuaderno. Claude Code no apareció en PATH. Se documentan ambos pasos pendientes; no se afirma una integración operativa.

La validación final y la referencia del commit se consultan en la entrada de cierre y `git log`. No se implementó código de producto. No se realizó push.

### Verificación del montaje

- `init.cmd`: código 0; estructura, integraciones, referencias y estados correctos. Aviso esperado: Claude Code ausente en PATH.
- `python -m unittest discover -s tests -v`: 9 pruebas correctas, incluidas denegación de entrega draft, tareas completadas, bloqueos, plan ausente, ejecutor incorrecto, alcance fuera del repositorio y múltiples features activas.
- `python -m pip check`: código 0, sin dependencias rotas.
- `specify integration list`: Codex y Claude instalados; Codex por defecto.
- Parseo de JSON: 11 archivos correctos; TOML validado por el verificador. Enlaces relativos de README/docs comprobados, sin destinos ausentes.
- `check_harness.py --implementation-ready handoffs/001-descubrimiento.json`: rechazo esperado, código 1, por entrega draft. No habilita construcción prematura.
- Primera ejecución directa de `init.ps1` bloqueada por política PowerShell de Windows; `init.cmd` verificado sin cambiar configuración global.
- Se inició `nlm login --storage protected`, que abrió Edge; requiere completar Google en el navegador. No declarar éxito hasta comprobarlo.

El montaje se realizó y revisó con Codex bajo la excepción inicial autorizada; esto no se presenta como una revisión independiente de producto.
