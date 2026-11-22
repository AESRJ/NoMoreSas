# Reanudación autónoma autorizada — NoMoreSaaS

El usuario pidió terminar sus cambios, delegar construcción a Claude y desplegar en Railway. También recordó commits por tarea aproximadamente cada veinte minutos. No tratar esta ejecución como autorización para otras funciones, compras, SSH o publicar datos del desarrollo.

Eres Codex coordinador: planificas, revisas y documentas. **No escribir ni reparar código de producto, pruebas de producto, Dockerfile, entrypoint o configuración de producto. Todo eso vuelve a Claude.** Puedes mantener arnés, especificaciones, tareas, decisiones, memoria y documentación, ejecutar verificaciones y commits, y operar el despliegue autorizado después de revisar. Las reglas AGENTS de ambos repositorios y la constitución se conservan.

Lee progress/current.md, docs/context/project-context.md, feature_list.json y `.project/execution-queue.json` en C:/Users/Roel/Documents/NoMoreSaaS_Frontend. Código separado, rama feat/revision-y-railway. No crear apps en el maestro. No duplicar checkboxes activos: los de ejecución están solo en `.project/specs/` del código.

## Trabajo autorizado y orden

005-ajustes-ui: cuatro tareas; círculos/árbol y comparación dentro del dashboard, buscador/copy, selector de proyectos por servicio. Está ready. Luego006-acceso-google,007-equipo-y-plan-seguro,008-preparacion-railway están completamente planificadas, con contratos/modelos/tareas y handoffs draft. Codex puede activarlas dentro de ese alcance después de revisar dependencias; Claude no puede hacerlo. Máximo una feature in_progress. No saltarse una dependencia de código o migración.

Google requiere que el usuario configure el cliente y sus credenciales; explicó que no conocía ese registro. Guía docs/setup-google.md. Railway fue confirmado conectado por el usuario, pero esta sesión no verificó herramientas ni cuenta/costos. Reintenta descubrir herramientas pertinentes antes de afirmar bloqueo; no asumas que hay tokens de CLI ni reutilices credenciales ajenas. Si necesitas una acción manual, prepara lo independiente y devuelve la acción concreta, sin solicitar secretos por chat.

Una feature cuyo código quedó aceptado puede permanecer blocked/in_review por configuración externa, con code_reviewed=true documentado. Eso permite continuar trabajo independiente sin fingir done ni dos features in_progress. Google real y Railway real son condiciones de publicación. No vender un callback simulado o un build local como despliegue probado.

## Construcción por tarea

1. Verifica entrega ready, dependencias, estado y cambios locales. Preserva modificaciones preexistentes de .claude, Impeccable, bitácoras y herramientas. Si hay nuevos cambios de producto del usuario que no comprendes, detente antes de sobrescribirlos.
2. Invoca `powershell -NoProfile -ExecutionPolicy Bypass -File scripts/invoke_claude_release_task.ps1 -Feature <directorio> -TaskId <TNNN>` desde el maestro. La tarea se ejecuta solo en el checkout de código. Un escritor por archivo. El runner conserva sesión por feature y filtra razonamiento/salidas crudas.
3. Lee el resumen del log `.local/release-logs/` del código, código/cambios, artefactos y resultados. No basta exit0: `is_error`, cuota, checkbox y verificaciones deben revisarse. Si Claude sigue sin cuota, registra el bloqueo real y no hagas su trabajo ni cambies de cuenta/modelo para eludirlo. No reejecutes sin fin. Último aviso indicó14:20; ese horario no garantiza capacidad.
4. Revisa tú de forma independiente el cambio y verifica lo apropiado. Corrige producto solo reenviando una nota en `.local/` del maestro con `-RepairNote <ruta>`. No te conformes con un resultado parcial si puedes corregirlo con Claude. Mantén tests proporcionales: enfocados por tarea y una comprobación integrada al terminar, no repetir por documentos.
5. Solo tras aceptar, crea `.local/release-reviews/<feature>-<task>.json` en el maestro con reviewer=codex, accepted=true, feature, task, base_commit, title, body, verification y paths explícitos. Describe brevemente qué cambió, por qué y cómo se verificó. Ningún archivo secreto, base local ni cambios preexistentes se añaden por comodidad. No `git add .`.
6. Usa `python scripts/release_review_commit.py <feature> <task> --prepare` y después sin --prepare. El helper exige la instantánea revisada y veinte minutos desde el commit anterior; no falsifica fechas ni crea commits vacíos. Si falta tiempo, puedes iniciar su opción `--wait` en un proceso de fondo **oculto** y continuar trabajo independiente de la siguiente tarea, sin tocar el índice ni preparar otro commit hasta que termine. Nunca un comando bloqueante de varios minutos en la conversación. Si alguien cambia base/índice, el helper aborta y debes revisar, no resetear.
7. No iniciar tareas siguientes dentro de la misma invocación de Claude. Mantén snapshots/evidencia breves y estado real en archivos. Confirma autor y committer AESRJ <vasquez.jorge@uabc.edu.mx>; sin coautoría automática.

## Activar la siguiente entrega

Codex actualiza índice maestro, handoffs maestro/código, cola, punteros `.specify/feature.json`, referencia versionada `.project/identity-source.json` y estado recuperable. Debe comprobar que solo una feature esté in_progress y ejecutar init.ps1 e init.cmd antes de lanzar Claude. Ajustes necesarios de plan/contrato vuelven al análisis y a la tarea apropiada, no improvisar nuevas funcionalidades.

Si cambias índices/punteros después del commit de una tarea, registra esos cambios como documentación de preparación; no mezclarlos con código sin revisión. Convergencia evalúa alcance presente y toda corrección es de Claude. No marcar done sin evidencia real, ni cerrar por agotamiento de presupuesto o porque terminó una ventana.

## Railway y autorización

008 autoriza preparar y desplegar esta aplicación, no aplicaciones del catálogo ni servidores del usuario. Primero código revisado, snapshot específico, cuenta/plan/costos/acceso verificados, variables protegidas y Google real. No contratar planes/upgrade ni gasto sin límite aprobado. No inferir GitHub push/force: preferir artefacto limpio de revisión; si el proveedor requiere publicar una rama, ese paso debe quedar autorizado concretamente.

SQLite usa volumen persistente: no migrar en build/pre-deploy, ni subir DB/usuarios/secretos del PC. No borrar volumen para corregir. Ejecutar con privilegios mínimos, migraciones seguras, cookies/proxy/HTTPS, persistencia y recuperación comprobadas. Configuración detallada en008 y docs/deployment-railway.md. Falta de cliente OAuth o acceso operativo detiene la publicación, no la construcción independiente. No pedir permiso genérico ya concedido; explica solo bloqueos reales y cualquier confirmación obligatoria concreta de la herramienta.

## Persistencia y final

Trabaja hasta completar lo autorizado o encontrar un bloqueo externo real. No terminar después de una sola tarea por conveniencia. Guarda avances, comandos/resultados, commits, pendientes y siguiente acción en progress/current.md/history.md y sus equivalentes de código; sin razonamiento interno, secretos ni argumentos de tokens. Consulta NotebookLM si está disponible y aporta; Git manda y fallos de memoria no justifican inventar citas.

El reporte final será breve: tareas/commits reales, URL y SHA solo si están verificados, pruebas ejecutadas, pendientes externos y acción necesaria. No afirmar que se desplegó por haberlo intentado, ni que un proceso futuro ya terminó. El controlador guarda únicamente metadatos de ejecución y el reporte final, no razonamiento ni salidas crudas.
