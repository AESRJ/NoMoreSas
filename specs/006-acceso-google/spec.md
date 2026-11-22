# Feature Specification: Acceso Google mediante OIDC y sesión privada
**Feature Branch**: feat/revision-y-railway
**Created**:2026-11-22
**Status**: Especificado; pendiente implementación/revisión externa cuando corresponda
**Input**: Feedback explícito del usuario y solicitud de implementar/desplegar enRailway, manteniendo Codexplanificador/revisor y Claudeconstructor.

## User Scenarios & Testing *(mandatory)*
### US1 — Entrar con Google (Priority: P1)
Una cuentaGoogle válida crea o recupera la misma identidad y sesión privada; cancelar vuelve al formulario con explicación.

**Why this priority**: Recorrido pedido por usuario.
**Independent Test / Acceptance**: Given contexto válido, When usuario realiza esta acción, Then Una cuentaGoogle válida crea o recupera la misma identidad y sesión privada; cancelar vuelve al formulario con explicación.

### US2 — Vincular mi cuenta existente (Priority: P1)
Una cuenta local mantiene proyectos y vinculaGoogle solo desde una sesión autenticada tras confirmar su contraseña.

**Why this priority**: Recorrido pedido por usuario.
**Independent Test / Acceptance**: Given contexto válido, When usuario realiza esta acción, Then Una cuenta local mantiene proyectos y vinculaGoogle solo desde una sesión autenticada tras confirmar su contraseña.

### US3 — Rechazar intentos inválidos (Priority: P1)
Código/token/estado vencido o repetido, correo enconflicto y sesióncambiada no crean accesos ni mezclan proyectos.

**Why this priority**: Recorrido pedido por usuario.
**Independent Test / Acceptance**: Given contexto válido, When usuario realiza esta acción, Then Código/token/estado vencido o repetido, correo enconflicto y sesióncambiada no crean accesos ni mezclan proyectos.

### Edge Cases
Errores/red/sesióncambiada oexpirada no pierden privacidad ni aplican respuestasobsoletas. Datos/configuraciónfaltantes se declaran; no simular resultados. Datosanteriores/proyectos/conexionesexternas se conservan; limitaciones de entorno sonexplícitas.

## Requirements *(mandatory)*
### Functional Requirements
- **FR-001**: Mantener acceso local y añadir entradaGoogle real cuando está configurado; sin configuración no simular éxito.
- **FR-002**: Crear identidad estable por(provider,sub), alta inicial con emailverificado; mismoGoogle conservausuario aunque cambie email externo.
- **FR-003**: No autoenlazar por coincidencia de correo: vinculación explícita con sesión y contraseña local actual; no duplicar ni transferir proyectos.
- **FR-004**: Proteger inicio/callback con CSRF/Origin, state/nonce/PKCE de un solo uso, expiración, tokens verificados y sesión regenerada.
- **FR-005**: Conservar hashes y proyectos existentes en migración; permitir cuentasGoogle sin contraseña local inventada.
- **FR-006**: Secretos y canje en servidor; scopes mínimos de identidad, sin guardar tokens/códigos ni pedir acceso aDrive/Gmail.
- **FR-007**: Verificar errores, persistencia/aislamiento y loginGoogle real cuando credenciales/consentimiento estén disponibles.

### Key Entities
Ver data-model.md; se conservan las entidades/propiedad existentes y solo las extensiones necesarias para este alcance.

## Success Criteria *(mandatory)*
### Measurable Outcomes
- **SC-001**: CuentaGoogle inicia sesión y accede solo a sus proyectos; logout revoca sesión.
- **SC-002**: Cuenta local existente conserva acceso/proyectos y puede vincularGoogle tras reautenticación; mismoemail por sísolo no concede acceso.
- **SC-003**: Callback inválido/vencido/repetido/cambiado no crea sesión ni vínculo; configuración ausente se comunica sin botónfalso.

## Assumptions
Una sola funcionalidad inprogress y un escritor porarchivo. Dependencias: UX-REVISION code reviewed. Toda configuración real externa debe verificarse, no se inventa. No push ni compras por inferencia. Commits por tarea revisada, intervaloaproximado20min solicitado explícitamente de nuevo porusuario; si tarea lleva más, verificar primero. No fechas falsas ni commitsvacíos. Constructor no se autoaprueba.
Manualhardwareconservada por confirmaciónal final; Outlinewiki y solicitudGoogle confirmadas. Windows es el primer diagnósticopropuesto dentro de007; configuraciónexternaGoogle/Railway y cuotas sondependencias deoperación, no ambigüedades delalcance.
