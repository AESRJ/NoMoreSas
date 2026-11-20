# Montaje paso a paso

Fecha inicial: 2026-11-19. Operador asistido: Codex, por solicitud expresa del usuario.

1. **Inspección.** `git status --short`, `git remote -v` y `git log` identificaron un repositorio sin commits, remoto `AESRJ/NoMoreSas` y PDF original sin seguimiento. No había código ni identidad Git configurada.
2. **Fuentes.** Se revisaron el [ejemplo de Betta Tech](https://github.com/betta-tech/ejemplo-harness-subagentes), [GitHub Spec Kit](https://github.com/github/spec-kit), sus guías de [Codex](https://github.github.io/spec-kit/integrations/codex.html) y [Claude](https://github.github.io/spec-kit/integrations/claude.html), la documentación de [subagentes Claude](https://code.claude.com/docs/en/sub-agents) y el [servidor NotebookLM](https://github.com/jacob-bd/gemini-notebook-mcp-cli).
3. **Entorno local.** `python -m venv .venv`; instalación de pypdf, specify-cli y notebooklm-mcp-cli. El primer intento sin red falló y se repitió con permiso. Las versiones quedaron fijadas en `requirements-tools.txt`; entorno y credenciales se excluyen de Git.
4. **Lectura del PDF.** Texto extraído de 13 páginas con pypdf y UTF-8. Original conservado; `docs/product/brief.md` separa MVP y futuro con páginas de referencia. No fue una inspección visual de maquetación.
5. **Spec Kit real.** `.\.venv\Scripts\specify.exe init --here --force --non-interactive --integration codex --integration-options '--events false' --script ps --ignore-agent-tools`. Se generaron skills oficiales y `.specify/`; no una imitación manual.
6. **Segundo cliente.** `.\.venv\Scripts\specify.exe integration install claude --script ps --integration-options '--events false'`. Se añadieron skills en `.claude/skills/`; Codex sigue por defecto. El aviso de archivos compartidos existentes era esperado: se conservaron los del paso anterior.
7. **Reglas y perfiles.** `AGENTS.md`, `CLAUDE.md`, constitución y siete especialistas. Codex planifica/revisa; Claude construye. No se lanzaron agentes ni se construyó producto.
8. **Estado.** Backlog, borrador de descubrimiento, plantilla de entrega y bitácora. La entrega permanece `draft`: falta decidir stack y primer incremento antes de crear plan técnico ejecutable.
9. **Memoria.** Instalados MCP y configuraciones de proyecto. `nlm login --check` confirmó que no existe perfil autenticado. Activación documentada en `docs/notebooklm.md`; no hay cuaderno creado ni fuentes cargadas.
10. **Verificación.** `init.ps1`, validación de entregas, pruebas del verificador y CI de Windows. La política de Windows bloqueó la invocación directa de scripts; se añadió `init.cmd`, que usa una política solo para su proceso, sin cambiar la global. Evidencia final en `progress/history.md`. Verifican el arnés, no la aplicación.
11. **Git.** Cuenta autenticada consultada: Israel Gomez Ahumada, `issgg`, ID 198836279. Se usa esa identidad y el correo noreply correspondiente solo para este repositorio. Primer commit previsto: `chore: montaje de arnés y estructura de agentes`. Consultar `git log -1 --format=fuller` para hash e identidad efectivos. Sin push automático.

## Continuar el registro

Cada sesión añade a `progress/history.md`: responsable, objetivo, pasos, archivos, decisiones, comandos con resultados, bloqueos y siguiente acción. Cambios de estructura o integración se documentan aquí; cambios de decisión requieren ADR. No reescribir la historia para simular que una integración pendiente funcionaba.
