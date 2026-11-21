# Iniciar construcción en Claude Code

Abrir una terminal nueva en la raíz de este repositorio para recoger Node, pnpm y Claude del PATH. Ejecutar `claude`; si el cliente pide confiar en el proyecto o aceptar el MCP, revisar y aceptar esa configuración. No pegar cookies, tokens ni claves.

Prompt de inicio:

```text
Lee CLAUDE.md, AGENTS.md y handoffs/002-catalogo-comparacion.json.
Ejecuta init.cmd y verifica la entrega con scripts/check_harness.py
--implementation-ready handoffs/002-catalogo-comparacion.json.
Trabaja en la rama feat/catalogo-comparacion sin descartar cambios existentes.
Usa /speckit-implement para implementar T001–T017 de
specs/002-catalogo-comparacion/tasks.md, siguiendo spec, plan y contratos.
Stack: React con Vite, React Router, Zustand, pnpm y Node.js con Express.
No sustituyas tecnologías ni amplíes el alcance a cuentas o despliegues.
Registra evidencia en progress/impl_MVP-CATALOGO.md y solicita revisión a Codex.
No marques la funcionalidad done ni cambies la autorización de la entrega.
```

Los comandos de aplicación se crearán durante T001; antes de eso, que `pnpm test` no exista no significa que las pruebas hayan fallado. El catálogo inicial requiere fuentes verificadas y pruebas de producto reales. El arnés y su verificador sí existen y deben pasar antes de empezar.
