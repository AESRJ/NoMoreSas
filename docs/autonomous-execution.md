# Ejecución autónoma por tareas

Solicitud del usuario: 2026-11-21. Ejecutar tareas de Spec Kit en autonomía y hacer commits individuales con intervalos aproximados de veinte minutos. Esta solicitud sustituye el límite anterior de dos commits para la nueva ejecución por tareas.

## Situación comprobada

La entrega `.project/handoffs/002-catalogo-comparacion.json` del repositorio de código está closed. T001–T017 están completadas en su tasks.md vigente. Los checkboxes del snapshot maestro no son una cola pendiente. No volver a ejecutar la entrega cerrada ni desmarcar tareas para simular avance.

Antes de arrancar otra implementación, Codex prepara spec, plan, tasks, análisis y entrega ready para el incremento elegido por el usuario. La pregunta pendiente es si continuar con diseño del catálogo usando Impeccable o con cuentas y proyectos. No elegir nuevas funciones por inferencia.

## Ciclo de ejecución

1. Comprobar rama, identidad AESRJ <vasquez.jorge@uabc.edu.mx>, cambios preexistentes, entrega ready y dependencias de la siguiente tarea. Conservar los cambios de instalación de Impeccable: no incorporarlos silenciosamente a un commit de producto.
2. Claude ejecuta una tarea de la entrega, con sus pruebas y documentación. Codex conserva planificación y revisión. Para UI, usar Impeccable conforme al brief.
3. Claude registra evidencia y devuelve el control a Codex. Codex revisa el diff y los checks afectados; cualquier corrección de producto vuelve a Claude.
4. Tras aceptación, crear un commit por tarea, indicando su ID, resultado y comprobaciones, sin coautoría automática. Incluir solamente sus archivos y evidencia. Si una tarea consiste en pruebas que deben fallar antes de otra tarea, distinguir ese resultado esperado de una regresión accidental y documentarlo antes del commit.
5. Procurar una separación aproximada de veinte minutos entre commits. Nunca fraccionar una tarea por el reloj, inventar fechas ni hacer commits vacíos. Si una tarea requiere más tiempo, terminar y verificar antes del commit. Si termina antes y todavía falta el intervalo, esperar de forma interrumpible antes del siguiente commit.
6. Persistir tarea actual, último commit, hora real y siguiente paso. Reanudar desde esa evidencia si se interrumpe la sesión. Terminar al agotar la cola ready o ante un bloqueo externo; no crear otra funcionalidad automáticamente.

## Permisos y continuidad

El permiso del usuario cubre la ejecución y los commits locales de las tareas acordadas. No implica push o despliegue. Las restricciones administradas del cliente siguen vigentes.

Este cliente tiene ProyectoWeb como raíz escribible; el código está en el checkout hermano NoMoreSaaS_Frontend. Para reducir aprobaciones de escritura, se necesita abrir el checkout de código como proyecto o incluir ambos checkouts en las raíces permitidas desde el cliente. Un AGENTS.md o un mensaje no cambia esa política.

Para Claude, usar reglas locales del proyecto y acceptEdits, permitiendo los comandos concretos de verificación necesarios. La ejecución anterior ya utilizaba permisos explícitos; no reutilizar su launcher: ordena completar la entrega 002 cerrada de una sola vez. El siguiente launcher debe recibir una tarea de la nueva entrega y devolver el control para revisión, sin ejecutar commits por su cuenta.

No hay un proceso periódico ni un programador de Windows activo creado por esta documentación. Los veinte minutos son una cadencia de la sesión de trabajo; continuar con el chat cerrado requiere configurar y comprobar aparte un ejecutor persistente y su mecanismo de revisión.

Referencias: [permisos de Claude](https://code.claude.com/docs/en/permissions) y [seguridad de Codex](https://developers.openai.com/codex/security/).
