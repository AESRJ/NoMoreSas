# Especificación de descubrimiento: NoMoreSaaS

Estado: borrador de producto, no listo para implementación. Fuente: `NoMoreSaaS.pdf`, pp. 4–12. Responsable: Codex.

## Escenarios del MVP que se deben dividir en incrementos

- US1: una persona selecciona un SaaS, consulta alternativas y compara sus capacidades y dificultad.
- US2: registra hardware y uso para obtener una estimación con supuestos y advertencias.
- US3: crea un proyecto con aplicaciones seleccionadas y obtiene un plan por etapas.
- US4: copia un prompt pertinente al paso actual y guarda el avance de su proyecto.
- US5: accede a sus proyectos mediante su cuenta sin acceder a los de otra persona.

## Requisitos de producto extraídos

| ID | Requisito | Fuente |
| --- | --- | --- |
| FR01 | Catálogo de SaaS y alternativas comparables | pp. 5–7, 12 |
| FR02 | Registrar hardware, usuarios, almacenamiento y necesidades de acceso | pp. 4, 7–8 |
| FR03 | Estimar configuración mínima y recomendada, y evaluar hardware existente | pp. 7–8 |
| FR04 | Plan de instalación por etapas con avance persistente | pp. 8, 10–12 |
| FR05 | Generar prompts con el contexto necesario para cada etapa | pp. 9–10 |
| FR06 | Detectar puertos en conflicto, recursos insuficientes, arquitectura incompatible y configuraciones inseguras | p. 10 |
| FR07 | Registro, inicio de sesión y varios proyectos por usuario | pp. 10–12 |

## Criterios de aceptación que deben concretarse por incremento

- Una alternativa muestra fuente y límites; una búsqueda sin coincidencias ofrece un estado comprensible.
- Una estimación identifica supuestos, datos desconocidos y unidades; no garantiza resultados a partir de ejemplos del PDF.
- Un plan conserva el orden y el progreso; su prompt no incluye secretos ni información innecesaria.
- Un usuario no puede consultar ni modificar proyectos ajenos.
- El MVP no ejecuta comandos ni se conecta a servidores reales.

Los umbrales de rendimiento, datasets, stack y casos concretos quedan pendientes en `docs/product/open-questions.md`. No inventar valores para completar el formato. El siguiente uso de Spec Kit debe generar una especificación acotada, un plan y tareas del primer incremento; este documento conserva la visión inicial.
