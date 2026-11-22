# Implementation Plan: Acceso Google mediante OIDC y sesión privada
**Branch**:feat/revision-y-railway | **Date**:2026-11-22 | **Spec**:spec.md

## Summary
Construir solo alcance especificado, por Claude una tarea por invocación; revisión/commits por Codex. Dependencias: UX-REVISION code reviewed.

## Technical Context
Stack existenteReact/Vite/Router/Zustand/pnpm, JS ESM, Express/SQLite/Argon2nativo Node26. No Next/Django/ORM ni cambiosglobales de herramientas.

## Constitution Check
PASS: especificaciónprevia, rolesestables, fuentes/supuestos, unaactiva, migración/reversión explícita si aplica, evidenciareal. Despliegue sólo aplicación008 pedido expresamente, no instalaciónremota de serviciosusuarios niSSH.

## Design & Project Structure
OIDC AuthorizationCode confidencial de Express, reutiliza cookie de sesión003. Inicio POST conCSRF/Origin devuelve URLGoogle; frontend usa navegación de página completa. EvitarSDK remoto/iframe innecesario; no tokensGoogle enZustand ni storageWeb. Scopes openid,email,profile y access_type=online. state y nonce aleatorios, PKCES256;5min/unuso ligados a presesión y propósito login|link. Consumir estado atómicamente y comparar nonce explícitamente tras verificarIDtoken con bibliotecaGoogle; verifyIdToken no sustituye esas comprobaciones.
Biblioteca google-auth-library: fuenteoficialmonorepo googleapis/google-cloud-node/core/packages/google-auth-library-nodejs; package consultado11.3.4/Node>=22, no afirmar última publicaciónNPM. Claude verifica versión publicada y fija paquete/lockfile compatibleNode26. No usar repo archivado como versiónactual.
ADR0008: separar credenciales locales en password_credentials; migración003 aditiva con transferencia exacta id/hash y ALTER TABLE users DROP COLUMN password_hash. No reconstruir usuarios conDROP/CASCADE ni inventar password paraGoogle. Prueba aislada de investigación enmemoria conSQLite local confirma que DROPdeesa columna funciona y conservaFK; Claude debe implementar y verificar migración completa desdeBD002 con usuarios/proyectos/secretos temporales, no asumir que el spike constituye prueba de producto. TablaUsers mantieneIDs/emails/createdAt, loginconsulta credentialstore. Auth externos se almacenan separados por sub.
Vinculación desde /cuenta para cuenta local autenticada, exige contraseña actual y CSRF antes de emitir transacciónlink. En callback requiere la misma cuenta; Googlevinculado a otroUUID→conflicto sin cambios; el GETcallback responde303 con reason=google_conflict (no409HTTP en navegación). EndpointsJSON pueden409 según contrato. No desvincular/fusionar/borrarcuentas eneste alcance. Google-only sin credencialpassword falla loginlocal con error genérico; no permitir crearpasswordporfallaOAuth.
ConfigGOOGLE_CLIENT_ID/SECRET/REDIRECT_URI solo servidor y todo-o-nada, callback explícito ligado a APP_ORIGIN. Dev http://127.0.0.1:5573/api/auth/google/callback; validar loopback real. ProducciónHTTPS estableRailway008, registrar URIexacta enGoogleCloud. No inferir callbackdesdeHost. Error/cancelación usa código interno y URLlimpia, nunca idtoken/code enlogs. MismaCookieHttpOnly/SameSiteLax, SecureHTTPS con proxyvalidado008.
Consentimiento/clienteGoogle deben crearse conusuario, sin solicitarsecretosporchat ni usarcredenciales deconectores. Prueba realpuede quedar externamentependiente tras código revisado: no declararfeaturedone solo con mocks, se puede continuar trabajoindependiente de007/008 manteniendo como blocked/in_review concode_reviewedtrue, no dosfeaturesinprogress.

## Phase0 Research / Phase1 Design
research.md, data-model.md, contracts/contract.md y quickstart.md. Fuentesprimarias; no pendiente de decisiones técnicas sin alternativa razonable. Activaciónserial segúncola; códigoaprobado convalidaciónexterna faltante se indica in_review/blocked, no done.

## Verification / rollback
Ver quickstart.md y tareas por riesgo. Pruebas enfocadas por tarea, lint/build y smoke final360/1280; no repetición masiva por cambiosdocumentales. DBs/puertos temporales3501/5773 o3351/5583, no preview3301/5573. Copia consistente antes de migrar DBreal, noreset/clean/dropdatos. Revertir app mediante commits revisados; restauración/migración sólo concompatibilidad comprobada, nuncadowngrade destructivo silencioso.

## Complexity Tracking
Solo dependencias y tablasjustificadas; detalles delalcance/valores de modelo canónicos se citan desde tasks. Documentar asistencia/comandos brevemente, sinrazonamiento interno ni secretos.

La migración003 incluye oauth_attempts ligado a hash de sesión. Consumir con DELETE RETURNING antes del canje, no un flag en JSON de sesión que dos callbacks puedan leer a la vez. Verifier efímero privado/TTL5min, limpieza de expirados; nunca tokens Google persistentes ni clientsecret en DB.

Aclaración de transporte2026-11-22: el callbackGET siempre termina303 a ruta interna limpia. Motivos internos permitidos: google_cancelled, google_failed, google_conflict; vínculo correcto /cuenta?reason=google_linked, login correcto /proyectos. Nunca copiar error_description, code/state/tokens ni mensajes del proveedor al destino. Conflictosnoautovinculan/nocambiancredenciales/proyectos. El409 corresponde a operacionesJSON cuando detectan conflicto directamente, no a un cuerpoHTML/JSON crudo del callback.
