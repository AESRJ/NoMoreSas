# Implementation Plan: Flujo final
**Branch**: feat/flujo-final | **Date**: 2026-11-22 | **Spec**: spec.md

## Summary
Completar prototipo local con catálogo actualizado, perfil privado, evaluación editorial y plan/avance persistente. Una entrega, siete tareas de Claude; Codex revisa/commitea cada una. Priorizar recorrido completo con controles esenciales, sin repetir toda la batería por cada cambio.

## Technical Context
React/Vite/React Router/Zustand/pnpm y Express/JavaScript ESM existentes. SQLite node:sqlite, sesiones/CSRF/ownership de003 reutilizados. Nuevas tablas con migración aditiva002; no reemplazar DB. Sin servicios externos obligatorios para planes; plantillas deterministas versionadas. Imagen mediante Higgsfield MCP registrado, pendiente aprobación/autenticación.
Code checkout: C:/Users/Roel/Documents/NoMoreSaaS_Frontend; maestro solo planificación. No paquetes nuevos salvo necesidad demostrada.

## Constitution Check
PASS planificación previa, funciones separadas, estimaciones explícitas, una feature activa, migración aditiva y sin acciones remotas. Cierre requiere evidencia independiente. Imagen dependiente no se cierra falsamente.

## Project Structure
apps/api/data: catálogo y reglas editoriales/fuentes. apps/api/src: validación, evaluación, planes y persistencia del flujo; migración en ruta existente.
apps/web/src: rutas/componentes del recorrido y API/store privados bajo patrones existentes. tests/e2e: smoke completo aislado. .project/: única lista ejecutable/evidencia.

## Phase 0: Research
Ver research.md: fuentes oficiales investigadas por agente de investigación; Outline BSL, Synapse element-hq, mínimos Immich actuales; WireGuard nativo. Presupuestos editoriales de desarrollo orientativos, no benchmarks.

## Phase 1: Design & Contracts
data-model.md y contracts/workflow.md definen validación, propiedad, fingerprint e invalidación. Ampliar API privada sin alterar respuestas antiguas de catálogo/proyectos salvo contenido del catálogo expresamente sustituido. Compatibilidad del plan no implica instalar servicios automáticamente.

## Verification and rollback
Cada tarea ejecuta su comprobación enfocada y registra resultado. Cierre: lint/build, regresión privacidad de API, smoke real del recorrido, persistencia tras reinicio y revisión visual360/1280. No repetir todos los e2e antiguos en cada tarea. Ajustar fixtures del catálogo retirado sin suprimir pruebas de seguridad. Tests y DB temporales; no usar datos del usuario. Migración aditiva, backup local antes de aplicarla al preview; rollback de aplicación conservando tablas sin DROP automático.

## Complexity Tracking
Sin nueva arquitectura distribuida ni dependencias de IA. ADR0006 registra estimación editorial/plantillas y sustitución del seed anterior.
