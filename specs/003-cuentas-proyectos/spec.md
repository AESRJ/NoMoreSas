# Feature Specification: Cuentas y proyectos privados

**Feature Branch**: `feat/cuentas-proyectos`
**Created**: 2026-11-21
**Status**: Especificada; decisiones técnicas en plan.md
**Input**: El usuario solicita cuentas y proyectos mediante tareas Spec Kit, implementación por Claude, revisión de Codex y commits individuales con descripción breve.

## User Scenarios & Testing

### User Story 1 - Acceder a mi cuenta (Priority: P1)

Como visitante quiero registrarme con correo y contraseña, entrar y salir de mi cuenta para conservar mis proyectos entre visitas.

**Why this priority**: Identifica al propietario antes de guardar información privada.
**Independent Test**: Crear una cuenta, salir, entrar y recuperar la misma identidad tras recargar.
**Acceptance Scenarios**:
1. Dado un correo nuevo y contraseña válida, al registrarme quedo identificado y puedo ir a mis proyectos.
2. Dadas credenciales incorrectas, al entrar recibo un mensaje genérico y no obtengo acceso.
3. Dada una sesión activa, al salir queda invalidada; recargar o reutilizar la sesión anterior no permite acceder.
4. Dada una sesión caducada, al intentar guardar recibo indicación de entrar nuevamente sin mostrar información privada de otro usuario.

### User Story 2 - Gestionar mis proyectos (Priority: P1)

Como usuario quiero crear varios proyectos con nombre, descripción opcional y alternativas del catálogo, consultarlos y modificarlos en visitas posteriores.

**Why this priority**: Es la base de los futuros planes por proyecto.
**Independent Test**: Crear dos proyectos, editar uno, reiniciar la aplicación y comprobar que persisten diferenciados.
**Acceptance Scenarios**:
1. Dada mi lista vacía, al abrir proyectos veo una explicación y acción para crear uno.
2. Dadas alternativas del catálogo, al crear un proyecto con nombre y selección válidos aparece en mi lista y su detalle.
3. Dado un proyecto propio, al editar nombre, descripción o alternativas se conserva el resultado al recargar.
4. Dado un fallo al guardar, permanezco en el formulario con mis valores y un mensaje recuperable; no aparece un éxito falso.

### User Story 3 - Mantener mis proyectos privados y eliminarlos (Priority: P1)

Como usuario quiero que mis proyectos sean exclusivamente míos y poder borrarlos mediante confirmación.

**Why this priority**: El aislamiento es parte esencial de cuentas, no un añadido posterior.
**Independent Test**: Con usuarios A y B, B no puede listar, leer, editar ni eliminar proyectos de A, ni manipulando sus identificadores.
**Acceptance Scenarios**:
1. Dado un proyecto de A, al consultar o modificar su identificador como B recibo el mismo resultado que para uno inexistente y no cambia el proyecto.
2. Dado mi proyecto, cancelar su eliminación no lo cambia; confirmar lo elimina y deja de aparecer tras reiniciar.
3. Dado un visitante, las rutas privadas no muestran proyectos y permiten entrar; el catálogo sigue disponible sin cuenta.

### Edge Cases

Correo duplicado con distinta capitalización; contraseña vacía, larga o con espacios; sesión caducada; cookie inválida; petición de escritura desde otro sitio; cuerpo desconocido o excesivo; nombres de proyecto repetidos permitidos; selección vacía, duplicada o desconocida; alternativa retirada posteriormente del catálogo; fallo de disco; envío doble; registro simultáneo del mismo correo; dos sesiones de usuarios distintos en un mismo navegador tras salir/entrar.

## Requirements

### Functional Requirements

- **FR-001**: Registrar con correo único y contraseña; iniciar y cerrar sesión, y consultar la identidad actual sin devolver contraseñas ni credenciales reutilizables.
- **FR-002**: Conservar cuentas, sesiones y proyectos tras reiniciar la aplicación; las sesiones expiradas o cerradas no autorizan acciones.
- **FR-003**: Mantener el catálogo y comparación públicos; exigir cuenta para cada operación de proyectos, tanto en la interfaz como en el servidor.
- **FR-004**: Crear, listar, consultar y editar proyectos propios con nombre, descripción opcional y una o más alternativas seleccionadas del catálogo.
- **FR-005**: Aplicar propiedad desde la identidad autenticada; nunca aceptar que el cliente elija propietario ni revelar proyectos ajenos mediante IDs, listados o errores.
- **FR-006**: Eliminar proyectos propios solo tras confirmación visible; borrar sus datos asociados y mantenerlos hasta que su propietario los elimine. No hay caducidad automática de proyectos.
- **FR-007**: Validar entradas y prevenir escrituras desde otros sitios, intentos de acceso ilimitados y exposición de credenciales por respuestas, errores o registros. Usar mensajes genéricos para credenciales incorrectas.
- **FR-008**: Formularios y navegación en español con etiquetas, foco visible y estados de carga, vacío, error y éxito distinguibles; utilizables por teclado a 360 y 1280 px. No perder valores ante errores recuperables.
- **FR-009**: Mantener seleccionadas las alternativas guardadas aunque después desaparezcan del catálogo, indicándolo sin inventar datos; no permitir guardar nuevas referencias desconocidas.
- **FR-010**: Verificar con pruebas automatizadas de autenticación, persistencia, aislamiento entre dos usuarios y recorrido de navegador, y mantener las pruebas del catálogo anterior.
- **FR-011**: Claude implementa una tarea por vez; Codex revisa antes de cada commit. Cada commit identifica tarea, cambio y validación brevemente, con autor y committer AESRJ. No publicar ni desplegar como efecto de esta entrega.

### Key Entities

- **Cuenta**: identidad privada asociada a correo y credencial protegida.
- **Sesión**: acceso temporal revocable a una cuenta.
- **Proyecto**: nombre, descripción, propietario y fechas; agrupa alternativas y no contiene aún hardware ni etapas de instalación.
- **Selección de proyecto**: alternativas elegidas, conservadas con el proyecto.

## Success Criteria

### Measurable Outcomes

- **SC-001**: El recorrido registrarse, crear proyecto, salir, entrar y recuperar el proyecto se completa en navegador y sobrevive al reinicio.
- **SC-002**: El 100% de los casos automatizados de lectura, edición y borrado cruzados entre dos usuarios son rechazados sin alterar proyectos.
- **SC-003**: Una sesión cerrada o vencida falla en todos los casos automatizados de operaciones privadas.
- **SC-004**: Los recorridos de cuentas y proyectos funcionan con teclado a 360 y 1280 px y siguen pasando las verificaciones del catálogo.
- **SC-005**: Cada tarea completada tiene su propio commit aceptado y una nota breve de verificación; las tareas incompletas permanecen visibles.

## Assumptions

- Incremento de desarrollo local; no despliegue público. Se elige correo/contraseña como opción mínima sin servicios externos; no recuperación por correo, verificación de correo, OAuth, MFA ni borrado de cuenta todavía. No presentar estas capacidades como disponibles.
- Los proyectos admiten varias alternativas y no son aún planes ejecutables; quedan fuera hardware, estimación, prompts, SSH, colaboración, importación y exportación.
- El catálogo no exige cuenta. Se resuelven Q05 y la retención/borrado de proyectos de Q08 para este incremento; exportación queda para otro alcance.
- Los límites, almacenamiento y controles concretos se definen en plan, modelo y contratos como decisiones revisables de Codex, sin atribuirlos al PDF.
