# Preparación de despliegue en Railway

Estado: plan008 definido, implementación y publicación pendientes. El usuario autorizó el despliegue; no hay servicio creado ni URL de producción verificados en esta sesión.

## Configuración propuesta

- Un servicio del monorepo: Express sirve frontend compilado y API.
- Puerto `PORT` de Railway e interfaz `0.0.0.0`.
- Dominio HTTPS generado por Railway, usado como `APP_ORIGIN` exacto.
- Un proceso y una réplica, SQLite persistente en `/data/nomoresaas/production.sqlite`.
- Volumen inicial dentro del límite real de la cuenta; no ampliar ni contratar sin límite de gasto aprobado.
- Migración al inicio con el volumen montado, después de preparar permisos y antes del healthcheck.
- Secretos nuevos de producción y credenciales Google en variables protegidas, nunca en el bundle o Dockerfile.

## Condiciones antes de publicar

1. Claude termina las tareas de005–008 y Codex acepta la revisión concreta.
2. Verificar cuenta/proyecto/plan/créditos de Railway y costo previsto. La confirmación de conexión del usuario no sustituye comprobar acceso operativo.
3. Completar cliente Google y URI de retorno para el dominio estable. Confirmar audiencia de la app Google.
4. Probar imagen Linux, Argon2 y SQLite nativos, ejecución con privilegios mínimos y cookies detrás del proxy.
5. Probar rutas directas,404JSON de API, ausencia de secretos/DB en estáticos, persistencia y respaldo recuperable.
6. Subir solo el snapshot revisado. No subir `.env`, DB local, configuraciones MCP ni archivos de usuario. Si el mecanismo requiere push a GitHub, resolver ese paso explícitamente; no hacer force.
7. Verificar la URL pública con un proyecto de prueba autorizado y registrar SHA, estado real y límites.

## Persistencia y recuperación

Railway no monta el volumen durante build o pre-deploy. Un healthcheck no evita la interrupción breve del redeploy con volumen. Respaldar SQLite de forma consistente y probar restauración en datos descartables; no copiar un `.db` abierto sin comprobar consistencia ni borrar el volumen para corregir un fallo.

La base de producción inicial será nueva. Migrar datos de desarrollo requiere una decisión aparte; no se suben automáticamente las cuentas del equipo local.

## Costo

La página consultada el22-11-2026 muestra créditos limitados en Free y un mínimo de USD5/mes en Hobby, con consumo adicional posible. No es una cotización de esta aplicación ni una promesa de servicio gratuito. Verificar plan y límites de la cuenta antes de contratar o ampliar gasto.

Fuentes: [volúmenes](https://docs.railway.com/volumes), [healthchecks](https://docs.railway.com/deployments/healthchecks), [pre-deploy](https://docs.railway.com/deployments/pre-deploy-command), [precios](https://railway.com/pricing).
