# Contexto recuperable

Actualizado: 2026-11-19. Proyecto: NoMoreSaaS. Remoto: `git@github.com:AESRJ/NoMoreSas.git`.

Objetivo: ayudar a descubrir alternativas open source y planificar su autoalojamiento. La fuente de producto es el PDF local de 13 páginas; su síntesis y dudas están en `docs/product/`.

Decisiones confirmadas: SDD con GitHub Spec Kit, Codex planifica y revisa, Claude Code construye, memorias en Git más NotebookLM, documentación paso a paso. Una funcionalidad activa y entregas por archivos. El arnés se montó con Codex por solicitud expresa; no hay implementación de la aplicación ni stack elegido.

Spec Kit 1.4.3 y NotebookLM MCP CLI 0.16.5 instalados en `.venv`. Ambos clientes tienen skills oficiales de Spec Kit y configuración MCP por proyecto. No se encontró `claude` en PATH. NotebookLM no tiene perfil `default` autenticado; conexión y cuaderno pendientes. No hay sincronización de fuentes realizada.

Siguiente acción: Codex resuelve Q01/Q02 y prepara el primer incremento usando Spec Kit. La entrega de descubrimiento permanece `draft`; Claude aún no tiene tareas listas de producto. Ver `progress/current.md` y `handoffs/001-descubrimiento.json`.
