# ADR 0004: destino de código y construcción autorizada

Estado: aceptado por instrucción del usuario. El usuario proporcionó `https://github.com/AESRJ/NoMoreSaaS_Frontend.git` y pidió adaptar un entorno separado e iniciar la construcción si la configuración estaba lista.

## Separación física y estructura

- Arnés maestro: `C:/Users/Roel/Documents/ProyectoWeb`, remoto AESRJ/NoMoreSas.
- Código: `C:/Users/Roel/Documents/NoMoreSaaS_Frontend`, remoto AESRJ/NoMoreSaaS_Frontend, checkout independiente sin repositorios anidados.
- El repositorio de código agrupa frontend en apps/web y backend en apps/api como workspace pnpm, siguiendo la recomendación anterior. El nombre Frontend del remoto no limita el alcance acordado a una sola aplicación.
- Documentación de ejecución, snapshot SDD, tareas y evidencia se agrupan en .project/. Reglas breves AGENTS.md/CLAUDE.md y configuración oculta de Spec Kit permiten trabajar sin mezclar el producto con el historial completo del arnés.

## Autoridad y coordinación

Este repositorio conserva planificación y decisiones de producto. El checkout de código conserva el snapshot identificado por .project/source.json; los checkboxes activos y evidencia de construcción pertenecen allí, no se actualizan dos listas simultáneamente. Cambios de alcance vuelven a Codex y requieren nueva revisión del snapshot. No hay sincronización automática bidireccional.

La entrega ready efectiva está en .project/handoffs/002-catalogo-comparacion.json del checkout de código. La entrega histórica en el arnés se cierra como transferida y referencia ese destino, sin autorizar implementación aquí. Codex prepara y revisa; Claude Code construye. El usuario reanudó expresamente la construcción en el destino.

## Configuración y límites

Repositorio nuevo comprobado vacío y con permisos de escritura; identidad local AESRJ <vasquez.jorge@uabc.edu.mx>. Base del entorno guardada en fbc49e0; rama de construcción feat/catalogo-comparacion. Configuraciones MCP con rutas propias del equipo permanecen locales e ignoradas. No se copian PDF, .venv, credenciales ni respaldo Git al repositorio de código.

Construcción autorizada: T001–T017 del catálogo público, React/Vite/Router/Zustand/pnpm y Express. Claude recibe permisos para edición, consultas de fuentes y comandos de desarrollo/pruebas; no se desactivan todas las comprobaciones de permisos. El constructor no hace push, despliegue, reset/clean ni cambios en otros repositorios. Tras la instrucción posterior del usuario de realizar el trabajo en automático, Codex revisa, integra y publica el incremento verificado en el remoto proporcionado, sin force ni despliegue. Los resultados se revisan antes de cerrar; crear el entorno no equivale a completar producto.
