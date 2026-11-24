# Revisión documental de los cambios de Claude

Fecha: 23 de noviembre de 2026. Autor de la investigación: Codex. Construcción atribuida a Claude según los informes del proyecto; autor y committer Git comprobados: AESRJ <vasquez.jorge@uabc.edu.mx>.

## Alcance y método

El usuario pidió investigar, documentar y publicar exclusivamente en el repositorio de agentes, además de actualizar NotebookLM. No se ejecutó Claude, no se cambió de rama, no se hizo fetch/pull/push en el código, no se ejecutaron pruebas de producto, migraciones, instalación ni despliegue. Se leyeron historial, diffs, fuentes y evidencias. `git ls-remote` solo consultó las referencias públicas. La comparación de contenido al cerrar esta revisión comprueba que el checkout de producto permanece intacto.

Código auditado: `AESRJ/NoMoreSaaS_Frontend`, rama `main`, HEAD `b217344623a8e41829fbd796f290239d998ae4f2`. La referencia remota main consultada coincide exactamente. La rama local `feat/revision-y-railway` sigue en `0e45470`; no representa los tres últimos commits de main. El repositorio de agentes es `AESRJ/NoMoreSas`; son destinos distintos.

## Commits nuevos identificados

El rango de investigación es `d2485ab..b217344`: siete commits posteriores a la importación de equipo ya revisada. El inventario de todos los archivos está al final.

| Commit vigente | Cambio y contenido principal |
|---|---|
| 9d2c713 | Evaluación por CPU/RAM/disco, procedencia y certeza, siguiente paso, fuentes/cálculos desplegables; prompts por etapas con seguridad, validación y recuperación. Incluye pruebas y tareas007 T003/T004. |
| 7944474 | Retira Google, página Mi cuenta, rutas y dependencia OIDC. Añade modo producción Express, SPA, PORT/interfaz pública, proxy acotado y cierre ordenado. |
| 0e4b0b7 | Dockerfile multietapa, entrypoint con volumen y cambio de usuario, .dockerignore, railway.json y runbook. |
| 0e45470 | Documentación de cierre y despliegue, bitácoras, decisiones y permisos ya existentes, marcas de tareas008 y permiso ejecutable del entrypoint. |
| 0a9aa3a | Añade startCommand explícito `/usr/local/bin/docker-entrypoint.sh` a railway.json para no arrancar la imagen con pnpm del monorepo. |
| 23eee50 | Mínimo de contraseña de 15 a 8 puntos Unicode, máximo128; validación API y formulario, pruebas asociadas. |
| b217344 | Retira importación JSON, recopilador Windows, descargas y pruebas del recopilador; conserva formulario manual y ayuda parcial del navegador. |

Fechas Git: 22-11-2026 entre23:00 y23:43 America/Tijuana. Los últimos commits se agruparon a intervalos inferiores a veinte minutos; no se presenta esa secuencia como cumplimiento de la cadencia anterior. T003/T004007 comparten commit y el retiroGoogle se combina con producción. No se reescribió la historia para separarlos.

## Comportamiento vigente

### Evaluación y planes

`apps/api/src/evaluation.js` recibe la procedencia persistida y devuelve `summary.resources` con requerido/disponible, ajuste, origen y certeza; `summary.nextAction` orienta hacia equipo, plan o edición del proyecto. Los datos aproximados mantienen el resultado pendiente de confirmar; no garantizan viabilidad. `workflow.js` evalúa lo guardado, no una procedencia sin guardar del formulario. Cambios de perfil/procedencia invalidan el avance mediante revisión y fingerprint.

Las reglas y plantillas pasan a `2026-11-22.2`. `plan-templates.js` define veinte etapas (cinco alternativas por cuatro fases) con comprobaciones previas, acciones, seguridad, validación y recuperación. `plan.js` compone el prompt con contexto pertinente, condiciones pendientes y fuentes; `WorkflowPage.jsx` muestra esos bloques. Se contemplan privilegios mínimos, secretos como marcadores, HTTPS, puertos necesarios, persistencia y recuperación. Son instrucciones orientativas: la app no ejecuta instalaciones ni comprueba por sí misma puertos, NAT o respaldos.

### Autenticación

Google ya no está disponible. Se eliminaron `google.js`, `google-auth.js`, GoogleSignIn, AccountPage, cliente account, rutas asociadas, pruebas y dependencia google-auth-library. `README.md` y el informe008 atribuyen el retiro a una decisión del usuario en la sesión de Claude; esta revisión observa el cambio y esa atribución, sin inventar una nueva instrucción de producto.

Las migraciones003/004 y las tablas relacionadas se conservan. No es una reversión de esquema. Si existen cuentas creadas exclusivamente con Google, ya no pueden iniciar sesión con ese proveedor; no se comprobó si hay cuentas reales afectadas, ni se consultó la base de datos. El registro y acceso actual son por correo y contraseña con Argon2id y sesiones persistentes. Los hashes e identificadores existentes no se reescriben en el commit de longitud.

Contraseña vigente: de8 a128 puntos Unicode, tanto en API como en formulario. El comentario de `passwords.js` todavía dice15: discrepancia documental. El mensaje de23eee50 atribuye ocho a NIST; no es correcto afirmar conformidad con la versión vigente para autenticación de un solo factor. NIST SP800-63B-4 exige15 en ese caso y permite8 cuando la contraseña forma parte de MFA. No se encontró MFA en el flujo revisado. Se documenta para decisión futura; esta auditoría no cambia la política ni implementa una corrección.

Fuente primaria contrastada el23-11-2026: https://pages.nist.gov/800-63-4/sp800-63b/authenticators/ y preguntas frecuentes https://pages.nist.gov/800-63-4-Implementation-Resources/faqs/ .

### Equipo y diagnóstico

El estado final de b217344 cambia el alcance que describía007: ya no hay importación JSON ni descarga/recopilador Windows. Se eliminaron `tools/diagnostic/`, los tres archivos de `apps/web/public/downloads/` y sus pruebas. `ProfileAssist.jsx` ofrece elegir este u otro equipo y, solo para este, leer datos aproximados del navegador. La lectura no guarda por sí sola: se muestran valores, se aplican al formulario y la persona guarda.

`diagnostic.js` conserva hardwareConcurrency como hilos disponibles, no núcleos físicos, y deviceMemory como RAM aproximada opcional. No obtiene un inventario completo ni el disco libre; no usa cuota del sitio como disco. El equipo remoto se declara manualmente. El backend conserva procedencia importada histórica para no perder datos. Quedan textos de evaluación y documentos que aún mencionan diagnóstico/importación; no se corrigen en producto por la instrucción de solo lectura.

### Preparación de producción y Railway

Express sirve API y SPA compilada en el mismo origen. Usa `PORT`, bind por defecto0.0.0.0 en producción, origen explícito o derivado de RAILWAY_PUBLIC_DOMAIN y trust proxy por saltos0–3 (por defecto1 en producción). Las API inexistentes siguen en404JSON y los enlaces profundos de la SPA reciben index.html; los archivos inexistentes con extensión no devuelven un index falso. Se añade caché de assets y cierre conSIGTERM. La configuración de origen y sesiones se valida antes de arrancar.

Dockerfile fija Node26.13.1-bookworm-slim/pnpm12.21.0, dependencias por lockfile, buildVite y runtime con dependencias API. La imagen final no incorpora el pnpm global de las etapas previas: de ahí el arranque explícito al entrypoint. `.dockerignore` excluye env, bases, configuracionesMCP, .local y herramientas. SQLite usa `/data/nomoresaas/production.sqlite`. El entrypoint prepara el directorio, asigna propiedad, cambia a usuario node mediante setpriv, migra y arranca. No migra durante build/pre-deploy. railway.json configura Dockerfile, healthcheck/api/health, timeout120 y reinicio ON_FAILURE con cinco intentos.

La guía de Claude pide volumen/data, SESSION_SECRET, dominio público y una réplica. Es una guía de configuración, no prueba de que existan esos recursos. El commit0a9aa3a describe un problema de start command observado en Railway, pero eso no acredita un despliegue exitoso. No se inspeccionó cuenta, volumen, costo, logs vivos ni URL pública en esta auditoría. GoogleOAuth dejó de ser una dependencia de publicación porque fue retirado.

## Evidencia de pruebas y límites

| Evidencia existente | Qué permite afirmar |
|---|---|
| Informe007 T003/T004: API enfocada52/52, webworkflow21/21, webcombinada45/45, lintPASS | Resultados declarados porClaude para esa implementación; su informe señala build/e2e/UI pendientes en esa sesión. |
| Informe008: lintPASS, API293/293, web193/193, buildPASS, e2e48/48 en1280/360, smokeproducción conDBtemporal | Resultados declarados porClaude antes de los dos últimos cambios. No se presentan como ejecutados porCodex hoy. |
| Informe008: sinDocker local | No consta build/ejecución real de la imagen, permisos del volumen enLinux ni persistencia tras redeploy real. |
| Commits23eee50/b217344 cambian pruebas además de código | Hay cobertura modificada, pero los totales293/193/48 anteriores no certifican por sí solos el HEADfinal. No se halló evidencia versionada nueva de suite completa para ambos commits finales. |
| Lectura de fuentes/diffs, gitls-remote, patch-id y comprobación de integridad del checkout | Verificaciones realizadas porCodex durante esta auditoría; sin ejecutar producto. |

No se ejecutaron suites ni comandos de desarrollo para respetar el checkout sin cambios y evitar cachés, artefactos o lecturas reales de hardware. No se declara100%funcional, seguridad auditada ni producción validada.

## Discrepancias de trazabilidad

1. El maestro mencionaba24d067f, ae58ad1 y06bf7f1: existen como objetos Git fuera de main. Sus patch-id estables coinciden respectivamente con9d2c713,7944474 y0e4b0b7. Son correspondencias comprobadas de parche; no se atribuye causa a la diferencia de hashes sin evidencia.
2. 2415d80 es un commit documental fuera de main, no el cambio de arranque. El arranque vigente está en0a9aa3a; el documental de main es0e45470. No equiparar esos parches sin comprobarlos.
3. `.project/execution-queue.json`, AGENTS/CLAUDE y handoffs del código conservan bloqueoGoogle/cuota semanal,007ready y008draft pese al contenido posterior. Tareas008 marcadas no acreditan release real. Se documenta aquí sin reparar ese checkout.
4. El maestro tenía handoff006 `cancelled`, valor no admitido por su verificador. Se representa el retiro como handoff `closed` con outcome `withdrawn`, no como Google funcional. El índice conserva estado compatible `blocked` con disposición retirada y sin requerir OAuth. No se modifica el verificador para aceptar un estado improvisado.
5. La documentación anterior sobre montaje de arnés y datos históricos permanece. Las decisiones0008/0009 y la condiciónGoogle de0010 quedan históricas mediante ADR0011. No se duplican checkboxes de ejecución en el maestro.
6. La orden actual es auditoría/documentación. Se puso enabled=false en la configuración local y se desactivaron las tres tareasWindows de reanudación, incluida23Nov23:01. Identidad/argumentos de los jobs se comprobaron antes. No hay constructor relanzado por esta revisión.

## Estado de aceptación después de esta revisión

- 005: cerrada previamente.
- 006: retirada en el código; su revisión histórica no implica proveedor vigente. No hay que configurar OAuth para el estado actual.
- 007: implementación observada con alcance reducido a manual/navegador y planes; revisión documental final registrada, sin declarar pruebas integradas nuevas ni independencia completa del cierre.
- 008: candidato de producción implementado; despliegue vivo, buildDocker y gates de persistencia/HTTPS/recuperación no verificados aquí.
- No hay nueva construcción autorizada en curso. Pendientes documentados, sin corregir producto ni desplegar.

## Paso a paso de esta auditoría

1. Leer estado, constitución e instrucciones de ambos repositorios; capturar HEAD/estado de producto y hashes de archivos versionados y no ignorados.
2. Comprobar historial local y main remoto sin actualizar código; estudiar el rango y los siete commits.
3. Contrastar archivos, informes y cambios de alcance; verificar equivalencia de tres parches y aclarar la referencia2415d80.
4. Contrastar la atribuciónNIST con fuentes primarias; registrar límites y pendientes sin reparar producto.
5. Detener únicamente automatismos propios antiguos para respetar solo lectura; actualizar estado/decisiones/handoffs documentales del maestro.
6. Actualizar NotebookLM con esta revisión y comprobar la fuente; registrar resultado real en bitácora.
7. Verificar arnés maestro, diff y conservación de producto; hacer commit en español comoAESRJ y push únicamente deNoMoreSas; comprobarSHAremoto.

## Inventario completo de archivos del rango

Estados Git: A añadido, M modificado, D retirado. Es un inventario histórico del rango, no una propuesta de archivos a editar. No reproduce secretos ni código de producto.

```text
M	.claude/agents/frontend.md
A	.dockerignore
M	.env.example
M	.gitattributes
M	.project/context.md
A	.project/design-tooling.md
A	.project/docs/decisions/0007-servicios-y-comparativa-integrada.md
A	.project/docs/decisions/0008-identidades-google.md
A	.project/docs/decisions/0009-diagnostico-local-revisable.md
M	.project/docs/deployment-railway.md
D	.project/docs/setup-google.md
A	.project/execution-permissions.md
M	.project/execution-queue.json
M	.project/progress/current.md
M	.project/progress/history.md
A	.project/progress/impl_DEPLOY-RAILWAY.md
M	.project/progress/impl_MVP-CATALOGO.md
M	.project/progress/impl_MVP-EQUIPO-ASISTIDO.md
M	.project/progress/review_AUTH-GOOGLE.md
M	.project/progress/review_MVP-EQUIPO-ASISTIDO.md
M	.project/specs/007-equipo-y-plan-seguro/tasks.md
M	.project/specs/008-preparacion-railway/tasks.md
M	AGENTS.md
M	CLAUDE.md
A	Dockerfile
M	README.md
M	apps/api/data/requirements.json
M	apps/api/package.json
M	apps/api/src/app.js
M	apps/api/src/auth.js
M	apps/api/src/config.js
M	apps/api/src/evaluation.js
D	apps/api/src/google-auth.js
D	apps/api/src/google.js
M	apps/api/src/passwords.js
M	apps/api/src/plan-templates.js
M	apps/api/src/plan.js
M	apps/api/src/server.js
M	apps/api/src/workflow.js
M	apps/api/tests/api.test.js
M	apps/api/tests/auth.test.js
M	apps/api/tests/db.test.js
M	apps/api/tests/evaluation.test.js
D	apps/api/tests/google-auth.test.js
M	apps/api/tests/plan.test.js
M	apps/api/tests/workflow.test.js
D	apps/web/public/downloads/nomoresaas-diagnostico-LEEME.txt
D	apps/web/public/downloads/nomoresaas-diagnostico.mjs
D	apps/web/public/downloads/nomoresaas-diagnostico.mjs.sha256
M	apps/web/src/App.jsx
D	apps/web/src/api/account.js
M	apps/web/src/api/auth.js
M	apps/web/src/components/AuthForm.jsx
D	apps/web/src/components/GoogleSignIn.jsx
M	apps/web/src/components/Layout.jsx
M	apps/web/src/components/ProfileAssist.jsx
M	apps/web/src/diagnostic.js
D	apps/web/src/pages/AccountPage.jsx
M	apps/web/src/pages/AuthPage.jsx
M	apps/web/src/pages/WorkflowPage.jsx
M	apps/web/src/store/auth.js
M	apps/web/src/styles.css
D	apps/web/tests/account.test.jsx
M	apps/web/tests/auth.test.jsx
M	apps/web/tests/diagnostic.test.jsx
D	apps/web/tests/google-login.test.jsx
M	apps/web/tests/helpers.jsx
M	apps/web/tests/workflow.test.jsx
A	docker-entrypoint.sh
M	package.json
M	pnpm-lock.yaml
A	railway.json
D	tests/e2e/account.spec.js
D	tests/e2e/google-login.spec.js
M	tests/e2e/identity.spec.js
M	tests/e2e/workflow.spec.js
D	tools/diagnostic/build.mjs
D	tools/diagnostic/nomoresaas-diagnostico.mjs
D	tools/diagnostic/test/collector.test.mjs
D	tools/diagnostic/test/fixtures/cim-hostile.json
D	tools/diagnostic/test/fixtures/cim-typical.json
```
