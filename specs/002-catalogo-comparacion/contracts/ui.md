# Contrato de interfaz

## Rutas

| Ruta | Comportamiento |
| --- | --- |
| `/` | Catálogo, búsqueda por nombre y acceso a SaaS/fichas |
| `/?q=texto` | Mismo catálogo filtrado; trim y comparación sin distinguir mayúsculas |
| `/saas/:id` | Nombre y alternativas relacionadas; ID desconocido muestra no encontrado |
| `/alternativas/:id` | Ficha con fuentes, fecha, licencia y evaluación editorial distinguida |
| `/comparar` | Dos o tres seleccionadas; si faltan, explica cómo seleccionar |
| Cualquier otra | Página no encontrada con enlace al catálogo |

## Selección y datos

Botones con nombre accesible que identifican la alternativa y su estado. Contador visible 0–3, acciones quitar y limpiar. Aviso accesible al alcanzar el límite o al retirar IDs inválidos. La navegación mediante enlaces del router conserva la selección; una recarga la reinicia deliberadamente. La recarga de una ficha debe seguir funcionando.

Búsqueda por Service.name o Alternative.name: normalizar trim y minúsculas. Si coincide SaaS, mostrar sus alternativas; si coincide alternativa, mostrarla y sus SaaS relacionados. No hay búsqueda semántica ni por contenido completo. Espacios vacíos equivalen a catálogo sin filtro. Mantener orden estable de la API.

Carga, error con reintento, catálogo vacío, búsqueda sin resultados y no encontrado son estados diferenciados. No convertir error en vacío. La capa de carga compartida no duplica el catálogo en Zustand ni repite fetch por cada pulsación.

## Presentación

Español, jerarquía de encabezados, formulario etiquetado, foco visible y avisos anunciables. En 360 y 1280 px no perder controles ni campos; la tabla puede tener desplazamiento horizontal propio claramente señalado. No prometer auditoría WCAG completa: comprobar los recorridos y documentar límites.

La comparación alinea nombre, capacidades, limitaciones, licencia, dificultad, notas de autoalojamiento y fuentes. Si no comparten servicio, mostrar que cubren necesidades distintas. Dato desconocido se muestra como desconocido, no como ausencia de la función. Enlaces externos HTTP(S), sin HTML arbitrario ni ejecución de contenido curado.

No añadir botones inactivos que aparenten cuentas, proyectos, estimación, instalación o generación de prompts ya disponibles.
