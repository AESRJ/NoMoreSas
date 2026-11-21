# Modelo del catálogo y selección

Modelo lógico del primer incremento. El JSON usa `schemaVersion: 1`, `services`, `alternatives` y `relations`; todas las referencias deben resolver. Ninguna escritura pública.

## Service

| Campo canónico | Restricción |
| --- | --- |
| `Service.id` | string slug ASCII minúsculas, patrón `^[a-z0-9]+(?:-[a-z0-9]+)*$`, 1–80 caracteres, único |
| `Service.name` | string no vacío, 1–120 caracteres tras trim |
| `Service.description` | string no vacío, 1–1000 caracteres tras trim |

## Alternative

| Campo canónico | Restricción |
| --- | --- |
| `Alternative.id` | mismo patrón/longitud de Service.id, único entre alternativas |
| `Alternative.name` | string no vacío, 1–120 tras trim |
| `Alternative.description` | string no vacío, 1–1000 tras trim |
| `Alternative.capabilities` | array de strings no vacíos, al menos uno, máximo 20; cada string <=500 caracteres |
| `Alternative.limitations` | array máximo 20 strings no vacíos <=500; puede estar vacío si se indica la ausencia de revisión en fuentes |
| `Alternative.license` | objeto con `label` no vacío <=120, `url` HTTP(S) y `classification` en `open-source`, `source-available`, `unknown`; solo open-source entra en el seed publicado |
| `Alternative.difficulty` | objeto con `level` en `basic`, `intermediate`, `advanced`, `unknown`; `explanation` string no vacío <=1000; se identifica como evaluación editorial |
| `Alternative.hostingNotes` | string 1–2000; explica requisitos documentados o declara que no se verificaron; no contener cifras inventadas |
| `Alternative.officialUrl` | URL absoluta HTTP(S), no javascript/data/file |
| `Alternative.documentationUrl` | URL absoluta HTTP(S) |
| `Alternative.sources` | array no vacío de Source; debe respaldar los datos publicados; no mezclar fuente oficial y evaluación editorial sin distinguirlas |

## Relation

| Campo canónico | Restricción |
| --- | --- |
| `Relation.serviceId` | referencia existente a Service.id |
| `Relation.alternativeId` | referencia existente a Alternative.id; pareja serviceId/alternativeId única |
| `Relation.coverage` | string 1–1000; necesidad cubierta y diferencias sin promesa de equivalencia total |

## Source

| Campo canónico | Restricción |
| --- | --- |
| `Source.url` | URL absoluta HTTP(S) |
| `Source.checkedAt` | fecha ISO `YYYY-MM-DD` válida, no posterior a la fecha real de curación |
| `Source.supports` | array no vacío de nombres de campos de Alternative que respalda; nombres desconocidos son error |
| `Source.kind` | enum `official`, `editorial` |
| `Source.note` | string <=1000; obligatorio no vacío para evaluación editorial y para explicar datos no verificados |

`Alternative.license`, `Alternative.difficulty` y sus propiedades se implementan como contratos indivisibles de los campos canónicos de esta tabla. En capacidades/limitaciones, una valoración editorial requiere motivo, nunca se disfraza de documentación oficial.

## ComparisonSelection

| Campo canónico | Restricción |
| --- | --- |
| `ComparisonSelection.ids` | array ordenado de 0–3 Alternative.id existentes, sin repetidos; compare requiere 2–3 |

Transiciones: añadir existente no cambia; añadir cuarto retorna límite sin mutar; retirar ausente no cambia; limpiar deja cero; reconciliar con catálogo elimina IDs inexistentes e informa cuántos se retiraron. No se persiste entre cierres/recargas de la SPA.

## Reglas de conjunto

- Dataset válido puede estar vacío para probar el estado vacío. El seed de demostración sí debe cumplir tres Service, cuatro Alternative y al menos dos alternativas para un mismo Service.
- Todo Service publicado tiene una relación y toda Alternative publicada tiene al menos una relación.
- Las reglas de campo y referencias se validan al iniciar; un seed inválido detiene el servidor con diagnóstico local. Nunca aceptar JSON arbitrario desde el usuario.
