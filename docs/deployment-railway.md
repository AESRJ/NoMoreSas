> Estado23-11-2026: copia documental del runbook deClaude en b217344. Sus pruebas son declaradas; no acredita despliegue vivo, recursos, costos ni instrucciones ejecutadas en esta sesión. Google fue retirado. Ver auditoría y ADR0011 antes de operar.

# Despliegue en Railway

Estado: artefactos de despliegue implementados y probados en local (modo producción con DB temporal). La imagen Docker no se construyó en esta máquina (sin Docker); Railway la construye desde GitHub. El acceso con Google se retiró.

## Qué hay en el repositorio

- `Dockerfile` multistage: `node:26.13.1-bookworm-slim` (tag verificado en Docker Hub), pnpm 12.21.0, `pnpm install --frozen-lockfile`, build de Vite y runtime solo con dependencias de producción de la API. No incluye `.env`, `.local`, DB, pruebas ni herramientas (`.dockerignore`).
- `docker-entrypoint.sh`: como root crea solo `$(dirname DATABASE_PATH)` y le da propiedad `node`; después baja privilegios (`setpriv`), aplica migraciones (`node src/db.js`, idempotente, nunca borra) e inicia la API.
- `railway.json`: builder Dockerfile, healthcheck `/api/health`, reinicio ON_FAILURE.
- Modo producción (`NODE_ENV=production`): bind `0.0.0.0`, puerto `PORT`, SPA servida desde `apps/web/dist` (deep links → `index.html`, assets con hash inmutables, `/api/*` desconocido y archivos inexistentes → 404 JSON), `trust proxy` = 1 salto, cookie `Secure` con APP_ORIGIN https, cierre ordenado con SIGTERM.

## Pasos en Railway (una vez)

1. Servicio conectado al repositorio `AESRJ/NoMoreSaaS_Frontend`, rama `main`. Railway detecta `railway.json` y usa el Dockerfile.
2. **Volumen**: añadir un volumen al servicio montado en `/data`. Sin volumen la base se pierde en cada despliegue.
3. **Variables** del servicio:
   - `SESSION_SECRET` = `${{secret(64)}}` (Railway genera un valor aleatorio; no cambiarlo después o se cierran todas las sesiones).
   - Opcional `APP_ORIGIN` = `https://<tu-dominio>` si usas un dominio propio. Si no se define se usa `https://$RAILWAY_PUBLIC_DOMAIN`.
   - No hace falta definir `PORT`, `NODE_ENV` ni `DATABASE_PATH` (la imagen fija `/data/nomoresaas/production.sqlite`).
4. **Networking → Generate Domain** para obtener la URL pública https.
5. Una sola réplica (SQLite es monoproceso).

## Verificación tras desplegar

- `GET /api/health` → `{"status":"ok"}`; `/` y un enlace profundo cargan la SPA.
- Registrar una cuenta de prueba, crear un proyecto, redesplegar y comprobar que sigue ahí (persistencia del volumen).
- Deploy Logs debe mostrar `[db] migraciones aplicadas…` y `[api] escuchando en http://0.0.0.0:<PORT>`.

## Errores típicos

- `SESSION_SECRET es obligatorio` → falta la variable.
- `APP_ORIGIN es obligatorio` → no hay dominio generado ni APP_ORIGIN.
- `No se pudo abrir la base de datos` → volumen no montado en `/data` o permisos; revisar el volumen.
- "Application failed to respond" → la app no arrancó; ver Deploy Logs.

## Respaldo y rollback

Antes de un despliegue con migraciones nuevas, crear un backup del volumen desde Railway (si el plan lo permite). Rollback de app: redesplegar un commit anterior compatible con el esquema; las migraciones son solo aditivas y nunca se hace downgrade automático. No borrar el volumen para corregir fallos.

La base de producción empieza vacía: las cuentas de desarrollo local no se suben.
