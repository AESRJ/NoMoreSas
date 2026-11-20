# NoMoreSaaS

Plataforma propuesta para descubrir alternativas open source, evaluar hardware y preparar planes de instalación y prompts por etapas. Fuente de producto: [NoMoreSaaS.pdf](NoMoreSaaS.pdf), 13 páginas.

Este repositorio contiene el entorno de desarrollo y su arnés de agentes. La aplicación todavía no está implementada.

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

El siguiente trabajo de Codex es resolver [las decisiones pendientes](docs/product/open-questions.md), especialmente el stack, y preparar la primera entrega de implementación. Abre Claude Code en esta carpeta una vez instalado; su CLI no se encontró durante el montaje.

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
