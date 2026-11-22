# Contrato entre herramientas

Crear un JSON desde `template.json`. `draft` no permite construir. Codex cambia a `ready` cuando spec, plan, tareas y verificaciones están completos; después puede pasar a `in_review` y `closed`. `blocked` indica una dependencia pendiente.

Los campos `task_ids` deben corresponder a tareas sin completar de `tasks.md`; `verification_commands` contiene comandos concretos del plan. `allowed_paths` delimita el alcance para Claude y revisión, pero no constituye una sandbox. Claude no modifica la autorización. Registrar el resultado en la ruta `implementation_report`; Codex revisa en `review_report`.

La entrega 001 de descubrimiento quedó cerrada al resolver stack y alcance. La entrega002 es histórica/cerrada. La entrega activa es `006-acceso-google.json`, lista operativa en `.project/` del código separado;005fue revisada/cerrada y suúltimocommitesperacadencia. Su estado ready significa que se puede empezar a construir; no declara funcionalidad ni pruebas de aplicación ya terminadas.
