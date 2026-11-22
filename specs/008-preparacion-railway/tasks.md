# Tasks: Preparación de producción y despliegue inicialRailway
Snapshot de planificación: ejecución/checkboxes SOLO .project/specs/008-preparacion-railway/tasks.md del código. Una tarea porinvocaciónClaude; Codex revisa y hacecommit. No autoaprobar.

## Phase1 Setup
Entorno/stack existente, no reinstalar ni cambiar componentes globales. Ejecutarinit/entrega y leer spec/plan/modelo/contrato antes de tarea.
## Phase2 Foundational
Dependencias: UX-REVISION code reviewed, AUTH-GOOGLE code reviewed; live config required before release, MVP-EQUIPO-ASISTIDO code reviewed. Un escritorporarchivo, no construcción de siguiente tarea en misma invocación.
## Phase3 Historias y entregas
Meta: las historias de spec.md y criterios observables de quickstart.md.
- [ ] T001 [US1] Construir modo producciónExpress (apps/api/src/config/server/app) que sirve apps/web/dist mismoorigen, GETSPA/404API correctos, PORT/bind y shutdown. data-model.md RuntimeConfig.mode, RuntimeConfig.port, RuntimeConfig.host, RuntimeConfig.appOrigin, RuntimeConfig.trustedProxyHops, RuntimeConfig.databasePath, RuntimeConfig.sessionSecret, RuntimeConfig.googleClientId, RuntimeConfig.googleClientSecret, RuntimeConfig.googleRedirectUri. Cookies/proxybounded y CSRF preservados. FR001/002. Verificar buildserverreal DBtemporal, deep links,secret/static/404 yheaders sin trustall.

- [ ] T002 [US2] Construir Dockerfile/.dockerignore/railwayconfig y entrypoint de arranque conNode/pnpmfijados, volumen/data, setupacotado y bajaprivilegiosantes de migración/API. data-model.md ReleaseRecord.replicaCount, ReleaseRecord.volumeMount, ReleaseRecord.backupReference. FR003/004/005. PruebasLinuxcrypto.argon2/SQLite,migraciónconBDexistente,volumenroot/nodeUID yrestart; no migrarenpredeploy, no.env/BDWindowsenimagen.

- [ ] T003 [US3] Añadir runbook y evidencia release .project/progress/impl_DEPLOY-RAILWAY.md con variables/nocredenciales, backup/restore,revision/container checks y pasos rollback. data-model.md ReleaseRecord.commit, ReleaseRecord.serviceId, ReleaseRecord.environmentId, ReleaseRecord.domain, ReleaseRecord.deploymentStatus, ReleaseRecord.spendLimit. FR005/006/007. Claude deja candidatepreparado, no crea recursos ni publica; Codex revisa/despliega solo cuando setup/costos/acceso permiten y validaHTTPS/Google/local/persistencia real. No marcar done con solo buildlocal.

## Phase4 Polish y cierre
Laúltima tarea incluyeintegración/checks/evidencia; Codex cierra sólo tras verificación, sin nuevos cambios de producto por Codex.
## Dependencies / strategy
T001 → T002 → T003. MVP primero porhistoria; no marcar próximas porinferencia. Paralelismo sololectura/investigación, nunca escritoresmismosarchivos. Bibliotecas/versiones/fuentes se verifican alinstalar. Condicionesexternaspendientes no seocultan.
