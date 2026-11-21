# Contrato HTTP

Mantener GET /api/catalog, /api/alternatives/:id y /api/health anteriores públicos y compatibles. JSON UTF8. Mutaciones requieren Content-Type application/json, Origin exactamente APP_ORIGIN y X-CSRF-Token de sesión; body máximo16KiB. Rechazar campos desconocidos con400, JSON inválido400, tamaño413, tipo415, origen/token403, sin sesión401, límites429, errores500 sin SQL/stacks/secretos. Envelope error existente {error:{code,message}}, añadir códigos sin romper catálogo. Respuestas de auth/proyectos Cache-Control:no-store. No CORS abierto, trust proxy falso local.

## Auth

- GET /api/auth/session →200 {user:null|{id,email},csrfToken}. Inicializa presesión solo si falta; cookie de sesión de servidor. Genera token y permite obtenerlo también tras caducar/reentrar. No contar lectura pública como login.
- POST /api/auth/register {email,password} →201 {user:{id,email},csrfToken}, auto login con regeneración. Duplicado409 mensaje de registro no disponible; restricciones400. Unicidad atómica incluso dos registros simultáneos.
- POST /api/auth/login {email,password} →200 mismo DTO; credenciales incorrectas401 con mensaje genérico idéntico. Regenerar y guardar sesión antes de responder; no reutilizar presesión.
- POST /api/auth/logout {} →204, destruir sesión y limpiar cookie con mismos atributos. Sin sesión válida401; cliente puede volver a GET session. El token antiguo/cookie antigua no autorizan escritura.

No retornar hash, sid, secreto de firma ni fechas internas de sesión. Cookie HttpOnly/Lax/Path=/ sin Domain, Secure según entorno; expiración servidor30min inactividad/24h absoluto. Token CSRF via JSON no es credencial de autenticación por sí solo.

## Proyectos autenticados

- GET /api/projects →200 {projects:[ProjectDTO]}, solo propios, orden updatedAt descendente e id ascendente como desempate. No paginación con máximo100; nunca listado global.
- POST /api/projects {name,description?,alternativeIds} →201 {project:ProjectDTO}. Máximo100 por cuenta, conflicto409. Rechazar ownerId/id/fechas extras.
- GET /api/projects/:id →200 {project:ProjectDTO}.
- PATCH /api/projects/:id {name?,description?,alternativeIds?} →200 {project:ProjectDTO}. Al menos un campo; campos omitidos se conservan. Validar selección completa existente cuando se envía.
- DELETE /api/projects/:id {} →204; borrado definitivo de proyecto y selección.

ID no UUID400. UUID válido ajeno o inexistente404 idéntico para GET/PATCH/DELETE, nunca403 que confirme existencia. Filtros de propietario en servidor y transacciones para selección/cupo. No aceptar propietario de body/query. Fallos dejan datos previos intactos.

ProjectDTO={id,name,description,alternativeIds,alternatives:[{id,name:null|texto,available:boolean}],createdAt,updatedAt}. Alternativa retirada se preserva como {id,name:null,available:false}; no inventar nombre. Sin ownerId ni datos de cuenta. Valores canónicos definidos en data-model.md.
