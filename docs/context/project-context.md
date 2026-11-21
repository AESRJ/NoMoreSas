# Contexto recuperable de NoMoreSaaS

Actualizado: 2026-11-20. Remoto: `https://github.com/AESRJ/NoMoreSas.git`. El original `NoMoreSaaS.pdf` y `docs/product/` describen la visión; el stack se confirmó directamente con el usuario en esta sesión, no se deduce del PDF.

## Reglas estables

Codex planifica y revisa; Claude Code construye. SDD con GitHub Spec Kit 1.4.3. Una funcionalidad activa, tareas/entregas persistentes y evidencia real antes de cerrar. Git conserva la autoridad; NotebookLM es memoria auxiliar con fuentes. No secretos en Git ni memoria. No push sin solicitud explícita.

Identidad Git confirmada por el usuario: **AESRJ <vasquez.jorge@uabc.edu.mx>** para autor y committer. Se corrigió la atribución errónea de los tres commits locales sin cambiar sus árboles, mensajes o fechas. Los hashes iniciales quedaron reemplazados; ver la corrección al final de `progress/history.md`. No inferir autoría desde cuentas conectadas a otras herramientas. La construcción está pausada por el usuario; la corrección de Git no la reanuda.

Autenticación verificada: GitHub CLI activo como AESRJ, confirmado por `gh api user`; acceso al remoto mediante `git ls-remote origin` por HTTPS correcto, sin refs porque sigue vacío. Credential helper y username AESRJ configurados solo en este repositorio; se utiliza el almacén seguro de GitHub CLI y no tokens en archivos del proyecto. No se eliminó la sesión de la otra cuenta ni se modificó la identidad global de Git.

## Tecnologías y alcance confirmados

Frontend: React, React Router, Zustand y pnpm, por tecnologías usadas en clase. Backend: Node.js con Express, elegido por el usuario. Plan de Codex: Vite, JavaScript ESM y workspace `apps/web` + `apps/api`. No Next.js ni Django. Primer incremento público: catálogo, búsqueda, ficha y comparación; catálogo JSON curado servido por API de lectura, sin cuentas ni base de datos todavía.

## Estado técnico comprobado

Claude Code 2.1.329 instalado/autenticado, Node LTS 26.13.1 y pnpm 12.21.0 instalados; ejecutar desde terminal nueva para recoger PATH. NotebookLM MCP CLI 0.16.5 en `.venv`, perfil protegido autenticado, cuaderno exclusivo **NoMoreSaaS - contexto de desarrollo**. PDF y AGENTS cargados; consulta con citas y prueba MCP stdio de notebook_get correctas. ID local en `.local/notebooklm.json`. Comprobación nativa: Codex reconoce el servidor habilitado; Claude reconoce la configuración de proyecto pero requiere aprobación inicial al ejecutar `claude`. No se ha dado esa aprobación por el usuario ni se afirma que Claude ya haya usado el servidor. No hay sincronización automática.

## Punto de reanudación

Descubrimiento cerrado mediante ADR 0002. `MVP-CATALOGO` activa en planificación entregada. `handoffs/002-catalogo-comparacion.json` ready; diseño completo y 17 tareas en `specs/002-catalogo-comparacion/`. No se ha escrito aplicación ni ejecutado sus pruebas. Claude toma T001–T017 y registra implementación; Codex revisa después. Continuar desde `progress/current.md`, sin reinicializar Spec Kit ni reemplazar tecnologías.

Los valores de diseño de catálogo/comparación se identifican como supuestos de Codex. Los datos candidatos requieren curación real por Claude. No prometer recursos de hardware a partir de ejemplos del PDF. Q04–Q08 corresponden a incrementos posteriores y no bloquean este catálogo público.
