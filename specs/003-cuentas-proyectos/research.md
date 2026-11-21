# Investigación y decisiones

Revisión 2026-11-21 por Codex e investigador delegado conforme speckit-plan. Runtime comprobado: Node26.13.1 exporta Database y crypto.argon2.

## SQLite

Decisión: archivo node:sqlite Database, journal DELETE, synchronous FULL, foreign_keys ON, busy_timeout5000, migraciones transaccionales versionadas y consultas parametrizadas. Motivo: persistencia sin otro servicio; monoproceso local. Alternativas: PostgreSQL añade infraestructura; JSON no ofrece integridad/concurrencia adecuada; bindings nativos duplican runtime. DatabaseSync es alias deprecated; módulo release candidate, síncrono. Sin WAL.

Fuentes: https://nodejs.org/api/sqlite.html ; https://sqlite.org/whentouse.html ; https://sqlite.org/pragma.html

## Contraseñas y abuso

Decisión: Argon2id asíncrono, memory19456KiB, passes2, parallelism1, salt16bytes y tag32bytes, guardar algoritmo/versión/parámetros. Máximo2 hashes concurrentes y rechazo429 si la cola supera10. Comparación constante, hash ficticio con coste equivalente para correo inexistente. Contraseña15–128 puntos Unicode sin trim/composición; correo trim/lowercase único, declarado y no verificado. Rate limit login por correo5/15min e IP20/15min, registro IP10/15min, limpieza TTL y máximo10000 claves; si se llena rechazar nuevas claves con429. Memoria local del limitador no garantiza control multiinstancia.

Fuentes: https://nodejs.org/api/crypto.html#cryptoargon2algorithm-parameters-callback ; https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html ; https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html

## Sesión y CSRF

Decisión: express-session, store SQLite get/set/destroy/touch; clave SHA256(sid) en DB, JSON del servidor sin password. resave:false y saveUninitialized:false. GET auth/session crea presesión asignando csrfToken32bytes; logout destruye y login/registro regeneran sesión, nuevo CSRF y guardado antes de responder. Secreto estable mínimo32bytes fuera de Git. Cookie HttpOnly/SameSite=Lax/Path=/, sin Domain, Secure HTTPS; HTTP explícito solo en loopback de desarrollo. Expiración servidor: inactividad30min y absoluto24h; reloj inyectable y cookie con expiración mínima de ambos. No tokens/contraseñas en localStorage/sessionStorage o Zustand persistido.

Toda mutación exige JSON y Origin igual a APP_ORIGIN más X-CSRF-Token sincronizador constante. GET no cambia proyectos. SameSite no basta. Alternativas descartadas: MemoryStore pierde persistencia; JWT complica revocación sin beneficio.

Fuentes: https://expressjs.com/en/resources/middleware/session/ ; https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html ; https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html

## Propiedad y alcance

owner_id desde sesión y filtros id+owner por operación; rechazar propiedad del cliente y campos extra; recurso ajeno/inexistente mismo404. Retener proyectos hasta borrado confirmado, sin exportación ni hardware todavía. Cuenta/verificación/recuperación y despliegue necesitan siguiente alcance operativo.

Fuente: https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html
