# Feature Specification: Preparación de producción y despliegue inicialRailway
**Feature Branch**: feat/revision-y-railway
**Created**:2026-11-22
**Status**: Especificado; pendiente implementación/revisión externa cuando corresponda
**Input**: Feedback explícito del usuario y solicitud de implementar/desplegar enRailway, manteniendo Codexplanificador/revisor y Claudeconstructor.

## User Scenarios & Testing *(mandatory)*
### US1 — Usar la aplicación porHTTPS (Priority: P1)
Un enlace público sirve SPA y API con login real, rutasdirectas y cookiesseguras bajo mismoorigen.

**Why this priority**: Recorrido pedido por usuario.
**Independent Test / Acceptance**: Given contexto válido, When usuario realiza esta acción, Then Un enlace público sirve SPA y API con login real, rutasdirectas y cookiesseguras bajo mismoorigen.

### US2 — Conservar proyectos al reiniciar (Priority: P1)
Base persistente y migraciones conrespaldo conservan usuarios/proyectos/avance trasrestart/redeploy.

**Why this priority**: Recorrido pedido por usuario.
**Independent Test / Acceptance**: Given contexto válido, When usuario realiza esta acción, Then Base persistente y migraciones conrespaldo conservan usuarios/proyectos/avance trasrestart/redeploy.

### US3 — Publicar revisión validada (Priority: P1)
Sólo código revisado entra al despliegue, configuración/secretos protegidos y límites/costos verificados, rollbackdocumentado.

**Why this priority**: Recorrido pedido por usuario.
**Independent Test / Acceptance**: Given contexto válido, When usuario realiza esta acción, Then Sólo código revisado entra al despliegue, configuración/secretos protegidos y límites/costos verificados, rollbackdocumentado.

### Edge Cases
Errores/red/sesióncambiada oexpirada no pierden privacidad ni aplican respuestasobsoletas. Datos/configuraciónfaltantes se declaran; no simular resultados. Datosanteriores/proyectos/conexionesexternas se conservan; limitaciones de entorno sonexplícitas.

## Requirements *(mandatory)*
### Functional Requirements
- **FR-001**: Servirfrontendcompilado yAPI enunservicio de producción sinVite dev/preview; rutasSPA/API yassetscorrectos.
- **FR-002**: Escuchar interfaz/puertodeRailway, HTTPSproxy confiable sintrustall, cookiesSecure yOriginCSRF exactos; shutdown ordenado.
- **FR-003**: SQLite en volumenpersistente conuna réplica/unproceso, migración alarranque convolumenmontado, datosprivados fuera delbuild.
- **FR-004**: ConstrucciónLinuxreproducible conversionesfijadas/lockfile y permisosruntime mínimos; no copiar módulosWindows ni secretos/DBlocal.
- **FR-005**: Healthcheck sólo listo trasconfig/migración/BD; respaldoconsistente y recuperación probada sin borrar datos reales.
- **FR-006**: Desplegar revisión concreta después derevisión y configuraciónOAuth/Railway/costos; verificar públicoHTTPS/auth/persistencia y no atribuirCIremota noejecutada.
- **FR-007**: Documentar dominio,variables no secretas,versión desplegada/costoobservado/límites/rollback; nada se publica si hay bloqueadores reales.

### Key Entities
Ver data-model.md; se conservan las entidades/propiedad existentes y solo las extensiones necesarias para este alcance.

## Success Criteria *(mandatory)*
### Measurable Outcomes
- **SC-001**: URLHTTPSpublica permite registro/loginGoogle/local segúnconfig, proyecto/equipo/plan/prompts/avance y rutasdirectas sin APIHTMLfalso.
- **SC-002**: Reinicio/redeploy conserva datos ysesiones conforme a contrato; restauracióndeprueba funciona desde respaldoconsistente.
- **SC-003**: Secretos/DBlocalno están enartefacto/bundle/logs y producciónnorequiereVite; despliegue se rastrea aSHArevisado.

## Assumptions
Una sola funcionalidad inprogress y un escritor porarchivo. Dependencias: UX-REVISION code reviewed, AUTH-GOOGLE code reviewed; live config required before release, MVP-EQUIPO-ASISTIDO code reviewed. Toda configuración real externa debe verificarse, no se inventa. No push ni compras por inferencia. Commits por tarea revisada, intervaloaproximado20min solicitado explícitamente de nuevo porusuario; si tarea lleva más, verificar primero. No fechas falsas ni commitsvacíos. Constructor no se autoaprueba.
Manualhardwareconservada por confirmaciónal final; Outlinewiki y solicitudGoogle confirmadas. Windows es el primer diagnósticopropuesto dentro de007; configuraciónexternaGoogle/Railway y cuotas sondependencias deoperación, no ambigüedades delalcance.
