# Implementation Plan: Preparación de producción y despliegue inicialRailway
**Branch**:feat/revision-y-railway | **Date**:2026-11-22 | **Spec**:spec.md

## Summary
Construir solo alcance especificado, por Claude una tarea por invocación; revisión/commits por Codex. Dependencias: UX-REVISION code reviewed, AUTH-GOOGLE code reviewed; live config required before release, MVP-EQUIPO-ASISTIDO code reviewed.

## Technical Context
Stack existenteReact/Vite/Router/Zustand/pnpm, JS ESM, Express/SQLite/Argon2nativo Node26. No Next/Django/ORM ni cambiosglobales de herramientas.

## Constitution Check
PASS: especificaciónprevia, rolesestables, fuentes/supuestos, unaactiva, migración/reversión explícita si aplica, evidenciareal. Despliegue sólo aplicación008 pedido expresamente, no instalaciónremota de serviciosusuarios niSSH.

## Design & Project Structure
ADR0010: usuario solicita explícitamente desplegar NoMoreSaaS enRailway. Esto revoca prohibición de despliegue paraeste servicio deaplicación trasrevisión; no autorizaSSH ni instalarservicios de proyectos deusuarios ni compras/upgrade sinlímiteaprobado. No otrorediseño de arquitectura: conservar monorepo, Expresssirve apps/web/dist y API mismoorigen enproducción. SinCORSnuevo, sinserviciofrontendindependiente, sinPostgres adicional paraMVP.
Dockerfile multistage enraíz, Node26.13.1 deimagenoficialDebian slim compatible ypnpm12.21.0fijados; Claude comprueba que tag existeyverifica crypto.argon2 nativo/node:sqlite enLinux. Noreferirse anpmnode-argon2, no dependenciabinariaWindows. Instalarfrozenlockfile/compilarVite, runtime sólo dependenciasnecesarias yartefactos, .dockerignoreexcluye.env/.local/.git/node_modules/SQLite/capturas/configsMCP. No incluir BD depreview niusuariosdemo.
Expressproducciónestática:APIroutes/errorhandlerantes del fallbackSPA; GET/api/inexistente404JSON; assetinexistente404noindexfalso. RutasSPA conocidas/deeplinks sirvencorrectoindexyReactcontrola acceso; archivosDB/.env/metadata nunca expuestos. Hashassetscacheimmutable/indexnocache.
PuertoRailwayPORT ybind0.0.0.0enprod; desarrolloactualno cambia. APP_ORIGINexactoHTTPSgeneradoestable,SESSION_SECRETnuevoestable sóloRailway,GoogleCLIENT_ID/SECRET/REDIRECT_URI sóloAPI. Proxytrustconfigbounded/verificado, no trueindiscriminado: política trusthop1 solamente sieseprueba coningresoRailwayreal; deotramaneradocumentartopologíayajustarantesaceptarlogin. CookieSecureHttpOnly/SameSiteLax,CSRF/Origin se conserva. SIGTERM dejaaceptarpeticiones/cierraDB sinorphan.
Volumen /data conarchivo /data/nomoresaas/production.sqlite yuna réplica/unproceso. Inicialmente0.5GBmáximo siFreeelegible y suficienteparaapp, verificarlímitereal; no suponerplanHobbycontratado. ElvolumenNOexisteenbuild/pre-deploy: entrypoint prepara subdirectorioexacto y migra antes de iniciarserver/health, nunca migrarSQLitedesdepredeploy. Railwaymontaroot; bootstraplimitadoa /data/nomoresaas yownershipsin777/recursivogenérico, después bajaprivilegiosaUIDnodepara migración+API. Esa soluciónespropuesta avalidar; documentar/operarRAILWAY_RUN_UID sólosi platformlo requiere, no dejarNoderootporcomodidad. Si no seprueba ejecuciónnonrootconvolumen deteneralpublicaciónhastaresolver.
SQLitebackupconsistenteprevio amigración/redeployconDBexistente, rollback deappcompatible con esquema o restore de respaldocon downtime; nunca DROP/wipe automáticamente. Railwaybackupmanual/programadosegúnplanaccesible, pruebaderestore enrecurso/DBdescartables; si no disponiblecrear procedimiento backupSQLiteconsistente, nogenerarcopiasdbincoherentes. Haydowntimebreveconvolumen, healthcheckRailwayesreadyde despliegue,no monitorcontinuo.
Publicar sólosnapshotgitSHArevisado mediante herramientaRailway disponible oCLIautenticada; preferirartefactodesde gitarchive sinsecretos/localuntracked. No gitpush/mergeforzado porinferencia: si RailwayrequiereGitHubsource/push distinto a publicación autorizada, presentar configuraciónconcreta alusuarioantes. No desplegar directo workingtreecon.env/BDlocal. No contraer suscripción/upgrade ni excedergasto aprobado; consultarplan/costosprimeroconexión. Usuario confirmaRailwayconectado, pero enesta sesión noaparecenaúnherramientas ycatálogopluginsmuestranotinstalled; no afirmar acce­sooperativo verificado.
Validarlocalproducciónfrente aDBtemporal yheadersproxy/confiables, buildDockerLinux si motoraccesible; faltaDockerlocal es dependencia deverificación, no fingir containerOK. Una vez códigoaprobado/config externa, operadorCodexrealizadespliegue yreviewvivo; Claude construyesoloartefactoscódigo sin crearcloud/compra. GoogleliveycredencialesGoogle sonreleasegate,nocerrarporfixtures. Ninguna cuenta local se sube sin autorización de migración de datos, produccióninicialvacía salvo datosyaexistentesRailwayque debenpreservarse.

## Phase0 Research / Phase1 Design
research.md, data-model.md, contracts/contract.md y quickstart.md. Fuentesprimarias; no pendiente de decisiones técnicas sin alternativa razonable. Activaciónserial segúncola; códigoaprobado convalidaciónexterna faltante se indica in_review/blocked, no done.

## Verification / rollback
Ver quickstart.md y tareas por riesgo. Pruebas enfocadas por tarea, lint/build y smoke final360/1280; no repetición masiva por cambiosdocumentales. DBs/puertos temporales3501/5773 o3351/5583, no preview3301/5573. Copia consistente antes de migrar DBreal, noreset/clean/dropdatos. Revertir app mediante commits revisados; restauración/migración sólo concompatibilidad comprobada, nuncadowngrade destructivo silencioso.

## Complexity Tracking
Solo dependencias y tablasjustificadas; detalles delalcance/valores de modelo canónicos se citan desde tasks. Documentar asistencia/comandos brevemente, sinrazonamiento interno ni secretos.
