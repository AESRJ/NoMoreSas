# ADR0005: Cuentas y proyectos locales

Fecha2026-11-21. Decisión técnica de Codex dentro del alcance autorizado de cuentas/proyectos. No atribuir elección de DB al PDF.

SQLite transaccional node:sqlite Database sobre Node26.13.1, Argon2id nativo y express-session persistente. Mantener stack de clase y Express. Sin JSON como DB, ORM o servicio PostgreSQL aún. SQLite release candidate y síncrono: monoproceso y desarrollo local; repositorios encapsulados para sustitución futura.

Correo/contraseña, sesión revocable/CSRF, proyectos privados con alternativas. Persisten hasta eliminación confirmada. Sin exportación, hardware o planes. Verificación/recuperación de correo, eliminación de cuenta y despliegue requieren revisión posterior. Catálogo sigue público.

Modelo y contratos en specs/003-cuentas-proyectos. Migración inicial sin datos previos. Reversión: detener API, conservar copia de DB y volver al código anterior; no borrar DB ni downgrade automático. Pruebas con DB temporal propia.
