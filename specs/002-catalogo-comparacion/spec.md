# Feature Specification: Catálogo público y comparación

**Feature Branch**: sin rama específica; el directorio de especificación es independiente de Git.

**Created**: 2026-11-20

**Status**: Especificado; pendiente de implementación por Claude Code.

**Input**: El usuario confirmó catálogo y comparación como primer incremento. Fuente de producto: NoMoreSaaS.pdf, páginas 5–7 y 12. Las tecnologías confirmadas por el usuario se registran en el ADR 0002 y en el plan, no se deducen del PDF.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Encontrar alternativas a un SaaS (Priority: P1)

Una persona visita el catálogo sin registrarse, busca el servicio que utiliza y encuentra alternativas con una explicación breve de qué necesidad cubren.

**Why this priority**: Permite demostrar el valor básico de NoMoreSaaS antes de pedir cuentas o datos de hardware.

**Independent Test**: Buscar un servicio presente en el catálogo, abrir sus alternativas y repetir con un término inexistente; ambas situaciones deben producir un resultado comprensible.

**Acceptance Scenarios**:

1. **Given** un catálogo publicado, **When** una persona entra, **Then** puede identificar los servicios SaaS disponibles y acceder a sus alternativas sin crear una cuenta.
2. **Given** el nombre de un servicio o alternativa existente, **When** lo busca con diferente uso de mayúsculas y espacios al principio/final, **Then** aparecen las coincidencias correspondientes.
3. **Given** una búsqueda sin coincidencias, **When** se ejecuta, **Then** se muestra un estado vacío con opción de restablecer la búsqueda.
4. **Given** que no es posible obtener el catálogo, **When** la persona entra o busca, **Then** ve un error comprensible y puede reintentar, sin confundir el fallo con un catálogo vacío.

### User Story 2 - Entender una alternativa y sus fuentes (Priority: P2)

La persona abre una ficha para comprender funciones, limitaciones, condiciones de autoalojamiento y origen de la información antes de considerar un cambio.

**Why this priority**: Una lista de nombres no permite tomar una decisión informada.

**Independent Test**: Abrir una ficha desde el catálogo o mediante su enlace directo y verificar los campos y enlaces de origen.

**Acceptance Scenarios**:

1. **Given** una alternativa publicada, **When** se abre su ficha, **Then** se muestran descripción, capacidades, limitaciones, licencia, dificultad explicada, documentación oficial y fecha de revisión de sus fuentes.
2. **Given** un dato que no fue verificado, **When** se muestra la ficha, **Then** aparece como no verificado o no disponible, nunca como un hecho confirmado.
3. **Given** un enlace de ficha inexistente, **When** se visita, **Then** se informa que no existe y se ofrece volver al catálogo.

### User Story 3 - Comparar opciones (Priority: P3)

La persona selecciona entre dos y tres alternativas y ve sus características alineadas para elegir qué investigar a continuación.

**Why this priority**: Convierte el descubrimiento en una comparación explícita y comprensible.

**Independent Test**: Seleccionar dos alternativas, compararlas, agregar una tercera y retirar una; comprobar que nunca se superan tres selecciones.

**Acceptance Scenarios**:

1. **Given** dos o tres alternativas distintas seleccionadas, **When** se abre la comparación, **Then** se muestran los mismos criterios para cada una y se identifica si atienden distintos servicios o necesidades.
2. **Given** menos de dos opciones, **When** se intenta comparar, **Then** se explica cuántas faltan; no se muestra una tabla vacía como resultado válido.
3. **Given** tres opciones seleccionadas, **When** se intenta agregar otra, **Then** se conserva la selección y se pide retirar una antes de añadir otra.
4. **Given** una selección existente, **When** la persona navega entre catálogo, ficha y comparación, **Then** la selección se mantiene durante esa sesión de navegación y puede modificarse o limpiarse.

### Edge Cases

- Catálogo sin registros, sin coincidencias, en carga o con error: estados distintos y recuperables.
- Selección repetida: no duplica la alternativa. IDs desconocidos o retirados: se informa y se conservan las opciones todavía válidas.
- Datos ausentes: no implican que una función no exista ni que dos alternativas sean equivalentes.
- Texto procedente del catálogo: se muestra como contenido, nunca se interpreta como instrucciones o código.
- En pantallas estrechas la comparación permite consultar todos los criterios sin ocultar opciones o controles.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: El catálogo DEBE ser público y ofrecer búsqueda por nombre de SaaS y alternativa, ignorando mayúsculas y espacios externos.
- **FR-002**: Cada SaaS DEBE mostrar qué alternativas están relacionadas con él y el motivo de la relación; no se garantiza equivalencia completa.
- **FR-003**: Cada ficha DEBE mostrar nombre, descripción, capacidades, limitaciones, licencia, dificultad con explicación, enlace oficial, documentación y fecha de revisión.
- **FR-004**: Todo dato evaluativo DEBE tener una fuente oficial o identificarse como evaluación editorial con motivo y fecha; lo desconocido DEBE indicarse explícitamente.
- **FR-005**: Se DEBEN poder seleccionar, retirar y limpiar hasta tres alternativas diferentes; comparar exige al menos dos.
- **FR-006**: La comparación DEBE mostrar criterios consistentes: capacidades, limitaciones, licencia, dificultad y requisitos de autoalojamiento documentados. Si las opciones cubren distintas necesidades, DEBE indicarse.
- **FR-007**: La navegación dentro de la sesión DEBE conservar la selección. No se exige conservarla al cerrar el navegador ni compartirla mediante enlaces en este incremento.
- **FR-008**: La interfaz DEBE distinguir carga, vacío, error y recurso inexistente, con una acción de recuperación apropiada.
- **FR-009**: El incremento DEBE funcionar en español, permitir operación mediante teclado y ofrecer nombres accesibles para búsqueda, selección y navegación.
- **FR-010**: El conjunto inicial DEBE cubrir al menos tres SaaS y cuatro alternativas verificadas; al menos un SaaS tendrá dos alternativas para demostrar una comparación pertinente.
- **FR-011**: Este incremento NO DEBE requerir registro, registrar hardware, estimar recursos personalizados, generar prompts, desplegar servicios ni ejecutar instalaciones.
- **FR-012**: Los escenarios US1–US3 y los errores relevantes DEBEN contar con verificación reproducible; el informe distinguirá pruebas automatizadas y comprobaciones visuales.

### Key Entities *(include if feature involves data)*

- **Servicio SaaS**: nombre, identificador estable, descripción y necesidad cubierta.
- **Alternativa**: identificador estable y datos de ficha verificables, relacionados con uno o más SaaS.
- **Relación de sustitución**: SaaS, alternativa, capacidades cubiertas y diferencias relevantes.
- **Fuente**: enlace oficial, fecha de revisión y dato al que respalda; distingue hechos de evaluaciones editoriales.
- **Selección de comparación**: conjunto ordenado de cero a tres alternativas distintas durante la navegación.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: El 100% de los tres SaaS iniciales permite llegar a por lo menos una ficha desde el catálogo sin iniciar sesión.
- **SC-002**: El 100% de las fichas publicadas identifica fuentes y fechas, o declara explícitamente los datos no verificados.
- **SC-003**: Todos los escenarios de selección con cero, una, dos, tres y cuatro opciones producen el resultado especificado; no hay duplicados.
- **SC-004**: Se completa el recorrido búsqueda → ficha → selección → comparación con teclado, y también en vistas de 360 px y 1280 px de ancho sin perder controles ni contenido necesario.
- **SC-005**: Las pruebas de aceptación verifican búsqueda, navegación, comparación, vacío, error y recurso inexistente; los fallos conocidos quedan registrados antes de solicitar cierre.

## Assumptions

- Se inicia con un catálogo pequeño y curado manualmente. Su composición concreta y sus fuentes se documentarán en el plan; no se importan datos masivamente ni se consultan servicios de terceros al navegar.
- Los mínimos de tres SaaS/cuatro alternativas, el máximo de tres comparables y los anchos de comprobación son valores de diseño propuestos por Codex para hacer este incremento verificable, no cifras extraídas del PDF.
- La selección no contiene datos personales. La persistencia entre sesiones, administración editorial y cuentas son trabajos posteriores.
- No se publican cifras de hardware sin fuente vigente y contexto; no se crea un estimador en este incremento.
- El stack confirmado es una restricción técnica del plan. La especificación expresa el comportamiento esperado independientemente de su implementación.
