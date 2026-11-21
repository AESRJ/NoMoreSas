# Arquitectura de trabajo y límites del producto

## Arnés implementado

Usuario → Codex (spec/plan/tasks) → entrega en disco → Claude Code (construcción y evidencia) → Codex (revisión). Git conserva las decisiones. NotebookLM consulta fuentes y resúmenes; no sustituye las tareas ni conserva el único ejemplar de una decisión.

Se usa GitHub Spec Kit oficial, instalado desde `specify-cli==1.4.3`, con integraciones Codex y Claude. Se desactivaron sus eventos nativos durante el montaje para mantener explícita la operación; la verificación se ejecuta con `init.ps1` y en CI. No hay hooks de bloqueo de herramientas ni aislamiento entre agentes.

## Módulos de producto propuestos desde el PDF

- Identidad y proyectos del usuario.
- Catálogo de SaaS y alternativas con fuentes y fecha de comprobación.
- Comparación y selección de aplicaciones.
- Inventario de hardware y perfil de uso.
- Estimación mínima/recomendada y validaciones de compatibilidad.
- Planes por etapas, prompts acotados y seguimiento del avance.

Son límites conceptuales; no implican microservicios. El 2026-11-20 se confirmó React + React Router + Zustand + pnpm y Node.js + Express. El primer plan utiliza Vite/JavaScript, dos aplicaciones en workspace pnpm y catálogo JSON validado de solo lectura. La autenticación, persistencia de proyectos y despliegue requieren planes posteriores. Ver ADR 0002 y `specs/002-catalogo-comparacion/plan.md`.

## Límites del MVP

Genera orientación y prompts que el usuario copia. No conecta SSH ni ejecuta instalaciones. Los números de hardware del PDF son ejemplos; no son reglas universales. Toda estimación debe incluir supuestos, unidad, fuente, fecha y tratamiento de incertidumbre. El alcance de catálogo inicial y la dependencia de modelos externos deben decidirse antes de implementar.
