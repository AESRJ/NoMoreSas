# ADR 0008: Google como identidad externa

Fecha: 2026-11-22. Alcance autorizado por el usuario; implementación pendiente de Claude.

Usar OIDC Authorization Code en Express, sesión existente y scopes de identidad mínimos. State, nonce y PKCE S256 se ligan a una transacción de cinco minutos y un solo uso. La aplicación verifica state y nonce explícitamente además de validar el ID token.

Identidad estable por Google `sub`; no enlazar cuentas automáticamente por correo. La vinculación exige sesión local y contraseña actual. El conflicto no debe transferir proyectos ni permitir acceso ajeno.

Extraer credenciales locales a `password_credentials`, conservar hashes e IDs y retirar solo la columna antigua después de copiarlos. Google no recibe una contraseña ficticia. Investigación aislada con SQLite en memoria comprobó viabilidad de esa operación; no sustituye las pruebas de migración de Claude con datos relacionados.

Los secretos quedan en servidor. No almacenar tokens Google en navegador, Git o memoria externa. Configuración real y login vivo son condiciones de aceptación separadas de las pruebas con fixtures. Ver spec006 y contrato.
