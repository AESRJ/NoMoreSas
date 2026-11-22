# Feature Specification: Equipo asistido y prompts claros con seguridad
**Feature Branch**: feat/revision-y-railway
**Created**:2026-11-22
**Status**: Especificado; pendiente implementación/revisión externa cuando corresponda
**Input**: Feedback explícito del usuario y solicitud de implementar/desplegar enRailway, manteniendo Codexplanificador/revisor y Claudeconstructor.

## User Scenarios & Testing *(mandatory)*
### US1 — Identificar equipo destino (Priority: P1)
Elegir detectar datosbásicos/importar diagnóstico/manual, revisar origen y datosfaltantes; no confundir navegador yservidor.

**Why this priority**: Recorrido pedido por usuario.
**Independent Test / Acceptance**: Given contexto válido, When usuario realiza esta acción, Then Elegir detectar datosbásicos/importar diagnóstico/manual, revisar origen y datosfaltantes; no confundir navegador yservidor.

### US2 — Importar datos reales sin teclearlos (Priority: P1)
Diagnóstico local revisable de sololecturaWindows produceJSONmínimo que rellenaperfil sin secretos ni ejecución desdearchivo.

**Why this priority**: Recorrido pedido por usuario.
**Independent Test / Acceptance**: Given contexto válido, When usuario realiza esta acción, Then Diagnóstico local revisable de sololecturaWindows produceJSONmínimo que rellenaperfil sin secretos ni ejecución desdearchivo.

### US3 — Entender resultado y próximos pasos (Priority: P1)
Evaluación resumeestado/motivos/acciones y cada fase proporciona prompt claro con seguridad, comprobación y recuperación.

**Why this priority**: Recorrido pedido por usuario.
**Independent Test / Acceptance**: Given contexto válido, When usuario realiza esta acción, Then Evaluación resumeestado/motivos/acciones y cada fase proporciona prompt claro con seguridad, comprobación y recuperación.

### Edge Cases
Errores/red/sesióncambiada oexpirada no pierden privacidad ni aplican respuestasobsoletas. Datos/configuraciónfaltantes se declaran; no simular resultados. Datosanteriores/proyectos/conexionesexternas se conservan; limitaciones de entorno sonexplícitas.

## Requirements *(mandatory)*
### Functional Requirements
- **FR-001**: Mantener manual como usuario confirmó; añadir ayuda parcial de navegador e importación voluntaria revisable para equipo destino explícito.
- **FR-002**: No prometer inventario completoWeb: CPUlógica/RAM aproximadas se identifican; cuotaweb nunca esdiscolibre; desconocidos no se inventan.
- **FR-003**: Ofrecer recopiladorWindows de sololectura del sistema, sin agentepermanente ni red; exportarJSONmínimo y no sobrescribir archivos existentes.
- **FR-004**: Validar importaciónesquema/tamaño/unidades/campos/rangos, sin ejecutar código ni subir identificadorespersonales; cambios se guardan explícitamente porpropietario.
- **FR-005**: Persistir procedencia y precisión de campos, conservar perfiles/proyectos existentes e invalidaravance cuando cambie perfil.
- **FR-006**: Evaluación explica aptitudorientativa/motivos/acciones primero y fuentes/cálculos desplegables; aproximaciones pendientes no garantizan viabilidad.
- **FR-007**: Cinco alternativas tienen prompts porfase con objetivo, contextojusto, precomprobaciones, acciones, seguridad, validación y recuperación; controles pertinentes sin secretos.
- **FR-008**: Sin instalacionesautomáticas/SSH ni afirmación de escaneo de red; pruebas y límites del SO/Node inicial explícitos.

### Key Entities
Ver data-model.md; se conservan las entidades/propiedad existentes y solo las extensiones necesarias para este alcance.

## Success Criteria *(mandatory)*
### Measurable Outcomes
- **SC-001**: Usuario importa diagnósticoWindows válido, revisa CPU/RAM/disco y guarda sin teclear esos datos; otroequipo/manual siguen posibles.
- **SC-002**: JSONinválido/ajeno/excesivo no ejecuta nada ni altera perfil; navegador incompleto sigue operativo sin inventar componentes.
- **SC-003**: Plan refleja solo perfilguardado y datosconprocedencia; cambio invalidaavance, seguridad/validación por etapa visibles en lascincoalternativas.

## Assumptions
Una sola funcionalidad inprogress y un escritor porarchivo. Dependencias: UX-REVISION code reviewed, AUTH-GOOGLE migration003 code reviewed. Toda configuración real externa debe verificarse, no se inventa. No push ni compras por inferencia. Commits por tarea revisada, intervaloaproximado20min solicitado explícitamente de nuevo porusuario; si tarea lleva más, verificar primero. No fechas falsas ni commitsvacíos. Constructor no se autoaprueba.
Manualhardwareconservada por confirmaciónal final; Outlinewiki y solicitudGoogle confirmadas. Windows es el primer diagnósticopropuesto dentro de007; configuraciónexternaGoogle/Railway y cuotas sondependencias deoperación, no ambigüedades delalcance.
