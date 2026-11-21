# NoMoreSaaS

Plataforma propuesta para descubrir alternativas open source, evaluar hardware y preparar planes de instalación y prompts por etapas. Fuente de producto: [NoMoreSaaS.pdf](NoMoreSaaS.pdf), 13 páginas.

Este repositorio contiene el entorno de desarrollo y su arnés de agentes. El primer incremento de la aplicación (catálogo y comparación) ya está implementado, revisado y publicado en main del repositorio de código; ver [revisión y evidencia](progress/review_MVP-CATALOGO.md). Preview de desarrollo local: http://127.0.0.1:5173.

Por decisión del usuario, **el código de la aplicación se construye en [AESRJ/NoMoreSaaS_Frontend](https://github.com/AESRJ/NoMoreSaaS_Frontend)**. Este repositorio conserva el arnés, las especificaciones, los planes y su documentación. El checkout de código está separado en `C:/Users/Roel/Documents/NoMoreSaaS_Frontend`; ver [ADR 0004](docs/decisions/0004-entorno-de-codigo-y-construccion.md).

## Inicio en Windows

```powershell
.\init.cmd
```

Si necesitas recrear las herramientas locales:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\bootstrap.ps1
.\init.cmd
```

Python 3.12 y Git son los prerrequisitos. La instalación necesita Internet. No es necesario activar el entorno virtual. `init.cmd` aplica la política de ejecución solo a ese proceso de PowerShell, sin modificar la política global de Windows.

## Cómo trabajamos

1. Codex lee `AGENTS.md`, el contexto y el estado de sesión; especifica, aclara, planifica y prepara tareas con GitHub Spec Kit.
2. Codex entrega un documento en `handoffs/` con estado `ready`, alcance, tareas y verificaciones concretas.
3. Claude Code lee `CLAUDE.md`, toma esa entrega y construye; registra cambios y evidencia en `progress/`.
4. Codex revisa el resultado. Una tarea se cierra con evidencia y revisión independiente.
5. Ambos dejan contexto persistente. NotebookLM ayuda a consultar fuentes; los artefactos aprobados permanecen en Git.

Stack confirmado: **React + Vite + React Router + Zustand**, paquetes con **pnpm** y API **Node.js + Express**. El usuario confirmó React/Router/Zustand/pnpm/Express; Vite y JavaScript forman parte del plan técnico de Codex. El primer incremento es catálogo público y comparación, con su diseño en [spec 002](specs/002-catalogo-comparacion/plan.md).

Claude Code 2.1.329, Node.js 26.13.1 y pnpm 12.21.0 instalados; Claude y NotebookLM autenticados. Abrir una terminal nueva después de los ajustes de PATH. La entrega histórica `handoffs/002-catalogo-comparacion.json` referencia el destino: la entrega ready para construcción y sus tareas activas están en `.project/` del repositorio de código; no ejecutar implementación en este repositorio.

## Mapa

| Ruta | Propósito |
| --- | --- |
| `AGENTS.md`, `CLAUDE.md` | Responsabilidades y reglas de cada herramienta |
| `.claude/agents/` | Especialistas de construcción y revisión |
| `.agents/skills/`, `.claude/skills/` | Skills oficiales de Spec Kit 1.4.3 |
| `.specify/` | Constitución, plantillas, scripts y flujo oficial SDD |
| `specs/` | Especificaciones y tareas por funcionalidad |
| `handoffs/` | Entregas explícitas entre Codex y Claude Code |
| `feature_list.json` | Índice del alcance; las tareas viven en `specs/` |
| `progress/` | Estado, informes y bitácora de sesiones |
| `docs/` | Producto, arquitectura, decisiones y montaje paso a paso |
| `.mcp.json`, `.codex/config.toml` | NotebookLM MCP por proyecto |
| `scripts/`, `.github/workflows/` | Verificación local y CI del arnés |

Consulta [la guía de operación](docs/workflow.md), [el montaje paso a paso](docs/setup-step-by-step.md) y [NotebookLM](docs/notebooklm.md). Inspirado en [el arnés de Betta Tech](https://github.com/betta-tech/ejemplo-harness-subagentes); no se copió su aplicación de notas.
