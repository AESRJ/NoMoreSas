# Modelo canónico

## User

- User.id: UUID generado servidor, PK inmutable.
- User.email: texto requerido trim/lowercase, 3–254 caracteres, patrón básico sin espacios con parte@dominio.ext, UNIQUE. Correo declarado, no verificado.
- User.passwordHash: formato versionado Argon2id con salt16bytes, tag32bytes, memory19456KiB/passes2/parallelism1. Nunca devolver o registrar. Contraseña de entrada15–128 puntos Unicode, sin trim ni truncado; no persistir texto original.
- User.createdAt: UTC ISO8601 generado servidor, inmutable.

## SessionRecord

- SessionRecord.idHash: SHA256 hexadecimal del sid de express-session; PK, no guardar cookie completa.
- SessionRecord.payload: JSON de sesión servidor, con csrfToken32bytes aleatorios, createdAt e userId opcional. Nunca password. ID de usuario válido para sesión autenticada.
- SessionRecord.expiresAt: timestamp UTC, mínimo entre última actividad+30min y createdAt+24h. Comprobar al leer/tocar; no revivir sesión expirada. Logout elimina registro; regeneración invalida el anterior. Datos expirados limpiados al iniciar y periódicamente con timer cerrado en tests.

## Project

- Project.id: UUID generado servidor, PK inmutable.
- Project.ownerId: FK User.id requerida, elegida exclusivamente desde sesión. Todas las consultas filtradas por ownerId; no retornarlo en DTO público.
- Project.name: texto trim, 3–80 puntos Unicode. Nombres repetidos permitidos.
- Project.description: texto trim, 0–1000 puntos Unicode, por defecto cadena vacía. No HTML ejecutable.
- Project.alternativeIds: array ordenado, 1–10 IDs únicos del catálogo existente al crear/editar. Rechazar desconocidos en escritura; al leer preservar retirados con available:false. Sin eliminar referencias históricas silenciosamente.
- Project.createdAt: UTC ISO8601 servidor inmutable.
- Project.updatedAt: UTC ISO8601 servidor al crear/editar.

ProjectSelection implementa Project.alternativeIds con project_id FK ON DELETE CASCADE, alternative_id y position UNIQUE por proyecto, sin FK al catálogo JSON externo. Cambios de campos/selección transaccionales, rollback ante error. Máximo100 proyectos por usuario; validar dentro de transacción para no sobrepasar por concurrencia. Borrar proyecto elimina selección.

## Config y migraciones

schema_migrations registra versión SQL aplicada una sola vez transaccionalmente. Índices UNIQUE de email, selección e índice owner/updatedAt. No contraseñas/sesiones en fixtures persistentes versionadas. Archivo configurado fuera de public/dist y Git; abrir archivo inválido falla claramente, nunca reemplazarlo por memoria.
