# Feature Specification: Flujo final del MVP NoMoreSaaS

**Feature Branch**: `feat/flujo-final`
**Created**: 2026-11-22
**Status**: Especificado; implementación pendiente
**Input**: Completar recorrido de proyecto, sustituir alternativas GitHub por Matrix, WireGuard y Outline wiki, conservar Google y aplicar paleta negra/lima con computadora central generada en Higgsfield. Claude construye; Codex planifica y revisa.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Elegir alternativas vigentes (Priority: P1)
Quiero explorar y comparar Nextcloud, Immich, Matrix/Synapse, WireGuard y Outline wiki para decidir qué incorporar a mi proyecto.
**Why this priority**: Es la entrada al recorrido.
**Independent Test**: Búsqueda/fichas/comparación públicas sin cuenta.
**Acceptance Scenarios**:
1. Given catálogo vigente, When busco GitHub/Gitea/Forgejo, Then no aparecen como opciones nuevas; siguen Nextcloud/Immich y aparecen las tres incorporaciones con fuentes y licencias correctas.
2. Given proyecto antiguo con alternativa retirada, When lo abro, Then conserva sus datos y explica que debo sustituirla antes de continuar el plan.

### User Story 2 - Evaluar mi equipo (Priority: P1)
Como propietario guardo hardware y uso esperado, y recibo una estimación orientativa con advertencias observables.
**Why this priority**: Evita presentar una instalación como viable sin revisar recursos.
**Independent Test**: Un proyecto con recursos insuficientes muestra motivos; uno con datos incompletos muestra compatibilidad pendiente.
**Acceptance Scenarios**:
1. Given proyecto propio, When guardo equipo/carga y recargo, Then conserva datos y muestra presupuesto desglosado, fuentes, fecha, supuestos y margen.
2. Given equipo incompatible o datos desconocidos, When evalúo, Then no declara compatibilidad garantizada ni oculta incertidumbre.
3. Given otra cuenta, When solicita esos datos o los modifica, Then no puede leerlos ni escribirlos.

### User Story 3 - Seguir un plan guiado (Priority: P1)
Como propietario consulto etapas por servicio, copio prompts y marco avances guardados para retomar el trabajo.
**Why this priority**: Completa el valor principal del MVP.
**Independent Test**: De proyecto nuevo a un paso completado; recarga y reinicio conservan avance.
**Acceptance Scenarios**:
1. Given proyecto evaluado, When abro plan, Then veo preparación, instalación prevista, comprobación y recuperación para cada selección, con enlaces y campos pendientes visibles.
2. Given etapa, When copio prompt, Then incluye contexto del proyecto, restricciones, fuentes y pasos de validación; un fallo del portapapeles ofrece selección manual sin fingir éxito.
3. Given avance guardado, When cambia equipo o selección, Then el avance anterior no se aplica silenciosamente al nuevo plan.

### User Story 4 - Recorrido visual coherente (Priority: P2)
Quiero una interfaz minimalista y profesional, negra y lima, con una computadora central en portada, usable también desde móvil.
**Why this priority**: Facilita revisar el flujo final solicitado.
**Independent Test**: Portada y recorrido privado a 360 y 1280 px, sin desplazamiento horizontal ni controles ilegibles.
**Acceptance Scenarios**:
1. Given cualquier vista, When navego, Then fondo negro, panel carbón, títulos blancos, texto suave/secundario y lima en acciones siguen la paleta exacta solicitada.
2. Given imagen Higgsfield disponible, When cargo portada, Then la computadora central se integra sin bloquear búsqueda o navegación. Si falta autenticación, se declara la dependencia y no se atribuye una imagen de otro origen a Higgsfield.

### Edge Cases
- Sesión caducada o cambiada: conservar separación entre usuarios y no aplicar respuestas obsoletas.
- Perfil incompleto, arquitectura desconocida, alternativa retirada: evaluación pendiente o bloqueada con motivo y siguiente acción.
- Cambios concurrentes: progreso de versión anterior rechazado, nunca trasladado al nuevo plan.
- Error de guardado: mensaje y reintento conservan valores; sin indicador falso de completado.

## Requirements *(mandatory)*
### Functional Requirements
- **FR-001**: Catálogo de cinco alternativas curadas, con las dos de Google conservadas y las tres nuevas correctamente descritas; retirar opciones GitHub sin borrar proyectos existentes.
- **FR-002**: Guardar perfil de hardware y carga por proyecto privado con validación de límites y acceso exclusivo al propietario.
- **FR-003**: Estimar recursos con cálculo reproducible, desglose por servicio, margen y separación entre referencia oficial y supuesto editorial fechado.
- **FR-004**: Advertir insuficiencia, requisitos de red/autenticación/licencias/almacenamiento, incompatibilidades y datos desconocidos, sin prometer instalación garantizada.
- **FR-005**: Mostrar plan guiado por etapas y servicio, enlaces oficiales y tareas previas concretas; WireGuard con instalación nativa y Matrix identificado como protocolo/Synapse como servidor.
- **FR-006**: Producir prompts copiables desde plantillas contextualizadas sin requerir claves de IA, instalar software o ejecutar acciones remotas.
- **FR-007**: Guardar avance privado, recuperarlo tras recarga/reinicio y vincularlo a versión de perfil, selección y reglas, rechazando escrituras obsoletas.
- **FR-008**: Integrar recorrido catálogo → cuenta → proyecto → equipo → evaluación → plan → prompts → avance, con estados de carga, vacío, error y navegación de retorno.
- **FR-009**: Usar #000000 fondo, #111111 panel, #FFFFFF títulos, #EEEEEE texto, #BDBDBD secundario, #C6FD0E acciones/íconos; computadora central solicitada a Higgsfield.
- **FR-010**: Conservar privacidad, revocación de sesión, protección de mutaciones y datos existentes; verificar lo esencial y registrar resultados reales y limitaciones.

### Key Entities
- Proyecto: propietario y alternativas; conserva referencias retiradas.
- Perfil: recursos declarados del equipo y carga prevista del proyecto.
- Evaluación: presupuesto orientativo, estado, advertencias y fuentes/versiones.
- Plan: etapas y prompts derivados de perfil y selección; versión identificable.
- Avance: pasos marcados por propietario para una versión del plan.

## Success Criteria *(mandatory)*
### Measurable Outcomes
- **SC-001**: Cinco fichas vigentes consultables y comparables; cero opciones nuevas de GitHub.
- **SC-002**: Un usuario completa todo el recorrido hasta copiar prompt y guardar avance; una segunda cuenta no accede a su información.
- **SC-003**: Perfil/avance reaparecen después de recarga y reinicio; cambio de configuración invalida avance anterior.
- **SC-004**: Escenarios insuficiente/desconocido muestran motivos y cero garantías falsas.
- **SC-005**: Portada y recorrido usables a 360/1280 px; dependencia de imagen pendiente no se reporta como terminada.

## Assumptions
- Prototipo local para revisar mejoras, sin despliegue, SSH, instalación de servicios ni compras.
- Se conservan cuenta/proyectos ya construidos. Prompts mediante plantillas, sin integración con modelos externos.
- La urgencia reduce repetición de pruebas; no elimina verificaciones de privacidad ni honestidad de resultados.
- Higgsfield necesita aprobación del servidor en Claude y autenticación real del usuario. El resto del incremento avanza independientemente.

## Clarifications
### Session 2026-11-22
- Q: ¿Cuál Outline? A: Wiki y documentación colaborativa, getoutline.com, confirmado por usuario.
