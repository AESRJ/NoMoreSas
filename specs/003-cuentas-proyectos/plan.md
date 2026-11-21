# Implementation Plan: Cuentas y proyectos privados

**Branch**: feat/cuentas-proyectos | **Date**: 2026-11-21 | **Spec**: spec.md

## Summary

Cuentas y CRUD privado de proyectos junto al catálogo público. Claude implementa seis tareas secuenciales con pruebas; Codex revisa y realiza un commit por tarea. Código en NoMoreSaaS_Frontend, snapshot operativo en .project/specs/003-cuentas-proyectos. No reabrir 002.

## Technical Context

JavaScript ESM, Node26.13.1, Express5, React/Vite, Router declarativo, Zustand y pnpm12.21.0 existentes. SQLite local node:sqlite Database (release candidate, síncrono), sin ORM, monoproceso y consultas acotadas. Argon2id asíncrono nativo; express-session y adaptador persistente SQLite. Versiones exactas verificadas por Claude antes de añadir dependencias. Vitest/Testing Library, node:test/supertest y Playwright existentes; fixtures temporales y reloj inyectable.

DB configurable, por defecto apps/api/.local/data/nomoresaas.sqlite con ruta absoluta estable; nunca en dist/public ni Git. Secreto de sesión mínimo32bytes generado fuera de Git, estable entre reinicios; APP_ORIGIN=http://127.0.0.1:5173 en desarrollo. Configuración ausente/inválida falla claramente sin fallback a memoria. Catálogo unitario createApp({catalog}) permanece operativo mediante auth opcional inyectada; servidor real requiere configuración nueva.

Objetivo local: dos usuarios concurrentes, hasta100 proyectos por cuenta, hasta10 alternativas por proyecto. Sin objetivo de carga productiva. Limitar cuerpo JSON16KiB, hashing concurrente2, consultas parametrizadas; no ejecutar contenido. API enlazada solo loopback como antes. Sin despliegue ni servidor PostgreSQL.

## Constitution Check

Antes y después del diseño PASS: alcance especificado, Codex planifica/revisa y Claude implementa; sin SSH/despliegue; evidencia por tarea y datos aislados. NotebookLM devolvió error de aprobación con policy never; usar fuentes locales y oficiales. No aclaraciones bloqueantes. ADR0005 registra persistencia y retención.

## Project Structure

Maestro specs/003-cuentas-proyectos/{spec,plan,research,data-model,quickstart,tasks}.md y contracts/{http-api,ui}.md. Copia operativa en .project/specs/003-cuentas-proyectos del código; solo allí checkboxes e informes activos.

API: src/{config,db,passwords,sessions,auth,projects}.js, migrations/001-identity.sql y tests/{db,auth,projects}.test.js. Web: api/{auth,projects}.js, store/auth.js, pages/{LoginPage,RegisterPage,ProjectsPage,ProjectPage,ProjectFormPage}.jsx y componentes propios. Integrar app/server/Layout/App sin romper catálogo. Nombres ajustables mínimamente con motivo en evidencia; contratos obligatorios.

## Phases and Gates

Research y decisiones en research.md. Diseño en modelo/contratos/quickstart. Seis tareas: DB; API auth; UI auth; API proyectos; UI proyectos; integración/seguridad. Cada una incluye pruebas afectadas, evidencia breve y revisión independiente antes de commit. Cadencia aproximada20min entre commits de implementación, sin forzar finalización prematura. Cierre con lint/test/build/e2e e init. No publicar. Migración inicial sin datos de cuentas previos; reversión deteniendo API, conservando copia de DB y volviendo al código anterior, sin borrar DB ni downgrade automático.

## Complexity Tracking

Sin excepciones constitucionales. SQLite experimental y síncrono es límite explícito del desarrollo local; encapsular repositorios para migrar después. Antes de producción revisar HTTPS, recuperación/verificación de correo, eliminación de cuenta y operación.
