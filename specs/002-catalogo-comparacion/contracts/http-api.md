# API de lectura del catálogo

Base de desarrollo: `http://127.0.0.1:3001`. La SPA consume `/api` mediante proxy local. JSON UTF-8, sin cookies ni autenticación en este incremento.

## GET /api/health

200: objeto `status` con valor `ok`. No revelar entorno, rutas o secretos. Un dataset inválido impide arrancar, por lo que no se responde salud correcta con datos inválidos.

## GET /api/catalog

200: objeto con `schemaVersion: 1`, `services`, `alternatives`, `relations` conforme a `data-model.md`. Orden estable por nombre y desempate por ID. Puede devolver arrays vacíos para estado vacío. No hay paginación en el dataset inicial ni filtro servidor: la búsqueda normalizada ocurre en cliente.

Sin datos de terceros en tiempo de petición. Una petición con query inesperada no cambia el contenido ni ejecuta operaciones; el frontend usa `q` en su propia URL, no como parámetro de esta API.

## GET /api/alternatives/:id

ID cumple la restricción de `Alternative.id`. 200: objeto `alternative` con la ficha y `relations` asociadas. 400 si el ID viola el patrón/longitud; 404 si es válido pero no existe. El frontend puede resolver la ficha desde la instantánea ya cargada; este endpoint sigue teniendo contrato y pruebas propios.

## Errores y métodos

- Objeto común: `error` con `code` estable y `message` legible en español.
- Códigos: `INVALID_ID` (400), `NOT_FOUND` (404), `INTERNAL_ERROR` (500).
- Rutas API desconocidas: 404 JSON, incluso para métodos no soportados. No habilitar escrituras. `HEAD`/`OPTIONS` pueden conservar el comportamiento HTTP estándar de Express; no afirmar que cambian datos.
- No devolver stack traces ni detalles internos en mensajes. Registrar diagnóstico técnico local sin secretos.
- Fijar `Content-Type` correcto, Helmet y desactivar `X-Powered-By`. No habilitar CORS abierto.
- Ningún endpoint instala software, consulta URLs proporcionadas por usuarios ni lee rutas arbitrarias de disco.
