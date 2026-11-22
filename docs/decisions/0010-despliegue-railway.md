# ADR 0010: despliegue inicial en Railway

Fecha: 2026-11-22. El usuario pidió implementar los últimos cambios y desplegar NoMoreSaaS en Railway.

La autorización cubre preparar y desplegar esta aplicación revisada. Sustituye la restricción anterior de no desplegar este MVP; no autoriza SSH, instalaciones de los servicios de usuarios, contratar planes ni ampliar gasto sin un límite aprobado. No implica un push a GitHub por inferencia.

Un servicio Express sirve la SPA compilada y la API bajo el mismo origen HTTPS. SQLite conserva una instancia y un volumen persistente `/data`. El volumen no está disponible en build ni pre-deploy: preparar permisos y migrar al arrancar, antes del healthcheck. Bajar privilegios antes de Node y probarlo; no dejar el proceso como root por comodidad.

Definir puerto/interfaz de Railway, proxy confiable verificado, cookies Secure, secretos protegidos, respaldo consistente y rollback. Hay interrupción breve al redeploy con volumen; no prometer alta disponibilidad.

El usuario confirmó conexión a Railway, pero el acceso operativo de esta sesión aún no está verificado. Consultar cuenta, plan, créditos y límites antes de crear recursos. Google y la aplicación completa deben pasar verificación real antes de declarar el despliegue terminado. No subir `.env`, DB de desarrollo, cuentas locales ni configuraciones MCP. Usar solo una revisión concreta aceptada.
