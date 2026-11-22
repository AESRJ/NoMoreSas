# Decisiones pendientes antes de construir

| ID | Decisión | Por qué afecta al trabajo | Responsable |
| --- | --- | --- | --- |
| Q01 | Resuelta para desarrollo: React + React Router + Zustand + pnpm; Node.js + Express. Vite/JavaScript en el plan. Producción queda para el incremento de despliegue | ADR 0002 | Confirmado por usuario 2026-11-20 |
| Q02 | Resuelta: catálogo público, fichas y comparación primero; seed candidato de tres SaaS/cuatro alternativas en la spec 002 | Entrega acotada y verificable | Confirmado por usuario; curación por Claude |
| Q03 | Resuelta para este incremento: dataset curado versionado y validado al arrancar; fecha/fuente por dato; revisión al modificar/publicar el seed, sin importación automática | Contratos y modelo de spec 002 | Codex; implementación por Claude |
| Q04 | Prompts por plantillas o generación mediante modelo externo | Costos, privacidad, claves y reproducibilidad | Usuario + Codex |
| Q05 | Resuelta para003: correo/contraseña, sesiones persistentes SQLite; catálogo sigue público. Sin despliegue ni recuperación/verificación de correo aún | ADR0005 y specs/003-cuentas-proyectos | Codex bajo alcance autorizado por usuario |
| Q06 | Rangos de estimación, unidades y margen de recursos | Evitar tratar ejemplos como garantías | Codex |
| Q07 | Sistemas operativos y arquitecturas de hardware soportados | Delimitar compatibilidad y planes | Usuario + Codex |
| Q08 | Resuelta parcialmente en003: proyectos privados retenidos hasta borrado confirmado; exportación y eliminación de cuenta pendientes de otro alcance | Modelo/contratos003 y ADR0005 | Codex bajo alcance autorizado por usuario |
| Q09 | Resuelta: login protegido, cuaderno exclusivo creado, PDF y AGENTS cargados; consulta con citas y prueba MCP reales correctas | Reactivar clientes para descubrir MCP; no hay sincronización automática | Usuario + Codex, 2026-11-20 |

Q04, Q06, Q07 y la parte futura de Q08 siguen abiertas para otros incrementos. Q05 y retención/borrado de proyectos se diseñan en003; producción requiere otra revisión. No asumir que el PDF eligió el stack: las tecnologías se confirmaron directamente en esta sesión.
