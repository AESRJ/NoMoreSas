# Tasks: Acceso Google mediante OIDC y sesión privada
Snapshot de planificación: ejecución/checkboxes SOLO .project/specs/006-acceso-google/tasks.md del código. Una tarea porinvocaciónClaude; Codex revisa y hacecommit. No autoaprobar.

## Phase1 Setup
Entorno/stack existente, no reinstalar ni cambiar componentes globales. Ejecutarinit/entrega y leer spec/plan/modelo/contrato antes de tarea.
## Phase2 Foundational
Dependencias: UX-REVISION code reviewed. Un escritorporarchivo, no construcción de siguiente tarea en misma invocación.
## Phase3 Historias y entregas
Meta: las historias de spec.md y criterios observables de quickstart.md.
- [ ] T001 [US2] Implementar también esquema de intentos de data-model.md OAuthAttempt.sessionHash, OAuthAttempt.stateHash, OAuthAttempt.nonceHash, OAuthAttempt.verifier, OAuthAttempt.purpose, OAuthAttempt.expectedUserId, OAuthAttempt.expiresAt, OAuthAttempt.returnTo, OAuthAttempt.consumed dentro de003. Implementar migración003 y repositorio de credenciales/identidades en apps/api/migrations y src: data-model.md User.id, User.email, User.createdAt,PasswordCredential.userId, PasswordCredential.passwordHash,ExternalIdentity.provider, ExternalIdentity.subject, ExternalIdentity.userId, ExternalIdentity.createdAt. Copiar hashes exactos antesDROPcolumn, conservarFK y datos003. Adaptarlogin/registro sin bajar seguridad. FR005. Verificar desdeDB002 conusuarios/proyectos,sesiones,rollback/cascada y loginlocal.

- [ ] T002 [US1] Implementar proveedor OIDC y endpoints start/callback/providers en apps/api/src, dependenciasfijadas package/lockfile. data-model.md OAuthAttempt.sessionHash, OAuthAttempt.stateHash, OAuthAttempt.nonceHash, OAuthAttempt.verifier, OAuthAttempt.purpose, OAuthAttempt.expectedUserId, OAuthAttempt.expiresAt, OAuthAttempt.returnTo, OAuthAttempt.consumed. CSRF/Origin,state/nonce/PKCE5minunuso, tokenverificado, alta/Googleexistente y rotación de sesión. FR001/002/004/006. Pruebas enfocadas negativos y persistencia sin tokens enlogs.

- [ ] T003 [US2] Implementar link/start con reautenticación contraseña/CSRF y callbackpropósito en API y /cuenta en web; data-model.md ExternalIdentity.provider, ExternalIdentity.subject, ExternalIdentity.userId y OAuthAttempt.expectedUserId, OAuthAttempt.purpose, OAuthAttempt.returnTo. Colisiónemail no autoenlaza, Googleyaajeno sinmutación; callback303reason=google_conflict,409soloendpointJSONsegúncontrato. FR003. Verificar2usuarios y conservación de proyectos/credenciales.

- [ ] T004 [US1] Añadir botón ContinuarconGoogle en registro/login y estados de cancelar/error/configausente, cuenta/vínculo y fallbacklocal en apps/web/src. Usarcontrato y rutasinternas; noSDK/tokenbrowser ni fingiractivación. FR001/006/007. .project/docs/setup-google.md y .env.example solo nombresplaceholder. Verificar UI/local y flujo de proveedor con fixtures; pruebavivaGoogle separada exige credencialesreales.

- [ ] T005 [US3] Integrar/pruebasriesgoauth, documentar setupGoogle/callbacks/estado y evidencia .project/progress/impl_AUTH-GOOGLE.md. FR001–007/SC001–003. Codex revisa; Googlelive no probado→in_review/blocked con dependenciaexterna, nunca donepormocks. Noeditar permisosCloud ni desplegar por cuenta propia.

## Phase4 Polish y cierre
Laúltima tarea incluyeintegración/checks/evidencia; Codex cierra sólo tras verificación, sin nuevos cambios de producto por Codex.
## Dependencies / strategy
T001 → T002 → T003 → T004 → T005. MVP primero porhistoria; no marcar próximas porinferencia. Paralelismo sololectura/investigación, nunca escritoresmismosarchivos. Bibliotecas/versiones/fuentes se verifican alinstalar. Condicionesexternaspendientes no seocultan.
