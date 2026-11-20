# Roles y uso de especialistas

| Rol | Herramienta | Responsabilidad | Entrega |
| --- | --- | --- | --- |
| Planificador y arquitecto | Codex | Requisitos, stack, contratos, tareas y entregas | `specs/`, `handoffs/`, ADR |
| Revisor final | Codex | Contrastar resultado con spec y evidencia | `progress/review_<feature>.md` |
| Implementador | Claude Code | Integrar tareas y construir la funcionalidad | Código e informe de implementación |
| Frontend | Claude Code | Interfaces, accesibilidad, estados y formularios | Código y evidencia UI |
| Backend | Claude Code | Persistencia, contratos y aislamiento por usuario | Código, migraciones y pruebas |
| Catálogo e infraestructura | Claude Code | Datos de aplicaciones, estimaciones y compatibilidad | Reglas y fuentes trazables |
| QA | Claude Code | Verificar aceptación y regresiones | Informe y pruebas; no autoaprobar |
| Seguridad | Claude Code | Revisar prompts, privacidad y configuración | Hallazgos, sin modificar el producto |
| Documentación | Claude Code | Documentar lo que efectivamente se construyó | Guías e informe de memoria |

Los especialistas son perfiles disponibles, no procesos arrancados permanentemente. Claude puede invocarlos explícitamente dentro de una entrega autorizada. Iniciar con implementador y QA; activar frontend/backend cuando se elija el stack, y catálogo/seguridad cuando el alcance los necesite. Evitar concurrencia en el mismo archivo. La coordinación entre herramientas se realiza mediante archivos; no existe un despachador automático Codex → Claude en esta versión.

Cada especialista lee los IDs y archivos de su tarea, trabaja sobre ese alcance y devuelve la ruta del informe. No transmite código completo entre conversaciones. Ningún especialista puede cambiar el estado de la entrega para darse autorización. Codex revisa, Claude corrige y el usuario decide las prioridades.
