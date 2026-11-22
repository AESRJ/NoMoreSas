# Feature Specification: Exploración por servicio y revisión de interfaz
**Feature Branch**: feat/revision-y-railway
**Created**:2026-11-22
**Status**: Especificado; pendiente implementación/revisión externa cuando corresponda
**Input**: Feedback explícito del usuario y solicitud de implementar/desplegar enRailway, manteniendo Codexplanificador/revisor y Claudeconstructor.

## User Scenarios & Testing *(mandatory)*
### US1 — Buscar un servicio conocido (Priority: P1)
Escribir Google Drive muestra su servicio y Nextcloud; el texto no exige conocer SaaS ni nombres de alternativas.

**Why this priority**: Recorrido pedido por usuario.
**Independent Test / Acceptance**: Given contexto válido, When usuario realiza esta acción, Then Escribir Google Drive muestra su servicio y Nextcloud; el texto no exige conocer SaaS ni nombres de alternativas.

### US2 — Abrir el árbol y comparar aquí (Priority: P1)
Un círculo accesible por teclado/táctil abre sus alternativas con animación; elegir una abre comparativa junto al servicio, sin pantalla aparte.

**Why this priority**: Recorrido pedido por usuario.
**Independent Test / Acceptance**: Given contexto válido, When usuario realiza esta acción, Then Un círculo accesible por teclado/táctil abre sus alternativas con animación; elegir una abre comparativa junto al servicio, sin pantalla aparte.

### US3 — Elegir reemplazos al crear proyecto (Priority: P1)
Nombre/descripción y búsqueda por servicio; chips servicio→alternativa permiten agregar/quitar varios sin duplicados, conservar edición y retiradas.

**Why this priority**: Recorrido pedido por usuario.
**Independent Test / Acceptance**: Given contexto válido, When usuario realiza esta acción, Then Nombre/descripción y búsqueda por servicio; chips servicio→alternativa permiten agregar/quitar varios sin duplicados, conservar edición y retiradas.

### US4 — Entender textos y contraseña (Priority: P2)
Título/bajada breves y ayuda de contraseña comprensible, sin rango técnico máximo ni cambio de política de seguridad.

**Why this priority**: Recorrido pedido por usuario.
**Independent Test / Acceptance**: Given contexto válido, When usuario realiza esta acción, Then Título/bajada breves y ayuda de contraseña comprensible, sin rango técnico máximo ni cambio de política de seguridad.

### Edge Cases
Errores/red/sesióncambiada oexpirada no pierden privacidad ni aplican respuestasobsoletas. Datos/configuraciónfaltantes se declaran; no simular resultados. Datosanteriores/proyectos/conexionesexternas se conservan; limitaciones de entorno sonexplícitas.

## Requirements *(mandatory)*
### Functional Requirements
- **FR-001**: Buscar servicios conocidos y conservar Google Drive→Nextcloud, Slack→Matrix/Synapse y Notion→Outline con búsqueda accesible y estados vacíos/errores.
- **FR-002**: Sustituir tarjetas SaaS por círculos con nombre y expansión de árbol; una alternativa por servicio es válida; teclado/táctil y movimiento reducido.
- **FR-003**: Mostrar comparativa servicio/reemplazo dentro del dashboard con fuentes y desconocidos explícitos; retirar sección global Alternativas, menú Comparar y banda de selección.
- **FR-004**: Conservar fichas y navegación directa antigua mediante redirección interna segura; no borrar catálogo, proyectos o referencias retiradas.
- **FR-005**: Crear/editar proyecto mediante búsqueda del servicio y chips de alternativas; selección1–10 única y separación entre usuarios existentes.
- **FR-006**: Simplificar título, bajada, buscador y ayuda de contraseña; conservar límites15–128, hashing, Unicode y reglas de login/registro.
- **FR-007**: Mantener computadoraHiggsfield/paleta aprobadas; no nuevos documentos de mejoraImpeccable; UIusable360/1280.

### Key Entities
Ver data-model.md; se conservan las entidades/propiedad existentes y solo las extensiones necesarias para este alcance.

## Success Criteria *(mandatory)*
### Measurable Outcomes
- **SC-001**: Usuario parte de GoogleDrive, veNextcloud y comparación en la misma página sin pasar por /comparar.
- **SC-002**: Usuario crea/edita proyecto con dos servicios y sus alternativas sin conocer sus nombres de antemano; quitar/repetir no duplica ni pierde datos.
- **SC-003**: Recorridos con teclado y360/1280 sin controles rotos ni desbordamiento; acceso/privacidad anteriores no cambian.

## Assumptions
Una sola funcionalidad inprogress y un escritor porarchivo. Dependencias: 004 cerrado; stack existente. Toda configuración real externa debe verificarse, no se inventa. No push ni compras por inferencia. Commits por tarea revisada, intervaloaproximado20min solicitado explícitamente de nuevo porusuario; si tarea lleva más, verificar primero. No fechas falsas ni commitsvacíos. Constructor no se autoaprueba.
Manualhardwareconservada por confirmaciónal final; Outlinewiki y solicitudGoogle confirmadas. Windows es el primer diagnósticopropuesto dentro de007; configuraciónexternaGoogle/Railway y cuotas sondependencias deoperación, no ambigüedades delalcance.
