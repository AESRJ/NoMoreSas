# Aviso solicitado al finalizar

22 de noviembre de 2026, 19:42 America/Tijuana. El usuario pidió aviso al terminar. Codex añadió infraestructura de notificación local; no modificó producto ni los archivos que está escribiendo el coordinador activo.

`scripts/watch-release-completion.ps1` observa el estado del controlador cada treinta segundos. Al finalizar intenta mostrar un mensaje de Windows únicamente en la sesión local que lo inició. Distingue cuatro funcionalidades terminadas de una ejecución que se detuvo con pendientes o errores; no presenta un bloqueo como proyecto completo. No envía correos ni mensajes externos.

Verificación: análisis de sintaxis PowerShell correcto; proceso oculto iniciado y comprobado, estado `watching` en `.local/release-finish-notifier.json`, PID39256. El controlador de construcción seguía `running`, PID16704. No se emitió un aviso de finalización durante la comprobación. La entrega efectiva del aviso solo se registra cuando Windows lo procese; requiere equipo y sesión disponibles. No es un mensaje automático dentro del chat.

Cambios de producto, revisión y commits siguen bajo el coordinador existente. Este observador no ejecuta tareas ni reinicia procesos.
