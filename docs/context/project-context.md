# Contexto recuperable de NoMoreSaaS

Actualizado: 2026-11-20. Remoto: `https://github.com/AESRJ/NoMoreSas.git`. El original `NoMoreSaaS.pdf` y `docs/product/` describen la visión; el stack se confirmó directamente con el usuario en esta sesión, no se deduce del PDF.

## Reglas estables

Codex planifica y revisa; Claude Code construye. SDD con GitHub Spec Kit 1.4.3. Una funcionalidad activa, tareas/entregas persistentes y evidencia real antes de cerrar. Git conserva la autoridad; NotebookLM es memoria auxiliar con fuentes. No secretos en Git ni memoria. No push sin solicitud explícita.

Identidad Git confirmada por el usuario: **AESRJ <vasquez.jorge@uabc.edu.mx>** para autor y committer. Se corrigió la atribución errónea de los tres commits locales sin cambiar sus árboles, mensajes o fechas. No inferir autoría desde cuentas conectadas a otras herramientas. La pausa posterior quedó revocada cuando el usuario proporcionó el repositorio de código y autorizó iniciar construcción allí (ADR 0004).

Autenticación verificada: GitHub CLI activo como AESRJ, confirmado por `gh api user`; acceso HTTPS correcto. El remoto inicialmente vacío ya recibió el avance autorizado en main: `a85a8d7ce6bdf338af76d851f90007485059860b`, con comparación local/remota correcta y sin force. Credential helper y username AESRJ configurados solo en este repositorio; se utiliza el almacén seguro de GitHub CLI y no tokens en archivos del proyecto. No se eliminó la sesión de la otra cuenta ni se modificó la identidad global de Git.

## Tecnologías y alcance confirmados

Frontend: React, React Router, Zustand y pnpm, por tecnologías usadas en clase. Backend: Node.js con Express, elegido por el usuario. Plan de Codex: Vite, JavaScript ESM y workspace `apps/web` + `apps/api`. No Next.js ni Django. Primer incremento público: catálogo, búsqueda, ficha y comparación; catálogo JSON curado servido por API de lectura, sin cuentas ni base de datos todavía.

## Estado técnico comprobado

Claude Code 2.1.329 instalado/autenticado, Node LTS 26.13.1 y pnpm 12.21.0 instalados; ejecutar desde terminal nueva para recoger PATH. NotebookLM MCP CLI 0.16.5 en `.venv`, perfil protegido autenticado, cuaderno exclusivo **NoMoreSaaS - contexto de desarrollo**. PDF y AGENTS cargados; consulta con citas y prueba MCP stdio de notebook_get correctas. ID local en `.local/notebooklm.json`. Comprobación nativa: Codex reconoce el servidor habilitado; Claude reconoce la configuración de proyecto pero requiere aprobación inicial al ejecutar `claude`. No se ha dado esa aprobación por el usuario ni se afirma que Claude ya haya usado el servidor. No hay sincronización automática.

## Punto de reanudación

Destino confirmado: AESRJ/NoMoreSaaS_Frontend, checkout `C:/Users/Roel/Documents/NoMoreSaaS_Frontend`. El arnés permanece aquí. El usuario autorizó construcción y trabajo automático; Codex preparó infraestructura, Claude implementó T001–T017 y Codex revisó e integró/publicó. MVP-CATALOGO done tras lint, 80 pruebas API, 56 frontend, build y 22 e2e correctas y capturas examinadas. CI del incremento 969baf1 aprobada en GitHub (run 44856440480). Entrega del código closed. Snapshot SDD, tareas y evidencia activos en .project/ del código; apps/web y apps/api separadas. feat/catalogo-comparacion integrada fast-forward en main; HEAD publicado f13e6d2b8b3167f53781e96ebc9e544e28284dae, local/remoto coincidentes. Preview http://127.0.0.1:5173 y API 3001. No crear producto aquí. Próxima funcionalidad necesita nueva especificación; ver progress/review_MVP-CATALOGO.md y ADR 0004. No hay despliegue de producción.

Los valores de diseño de catálogo/comparación se identifican como supuestos de Codex. Los datos candidatos requieren curación real por Claude. No prometer recursos de hardware a partir de ejemplos del PDF. Q04–Q08 corresponden a incrementos posteriores y no bloquean este catálogo público.

CI final de f13e6d2 confirmada success en run 44856563386. El catálogo inicial fue curado por Claude y revisado en el alcance descrito en los informes; las candidatas no revisadas de futuras ampliaciones siguen necesitando verificación. La API local respondió status ok después de publicar. El usuario prefiere ejecución automática de trabajo autorizado, manteniendo las aprobaciones impuestas por la plataforma y sin ampliar funciones por inferencia.
