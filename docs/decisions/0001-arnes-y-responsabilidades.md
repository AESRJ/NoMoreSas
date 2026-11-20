# ADR 0001: arnés, responsabilidades y memoria

Fecha: 2026-11-19. Estado: aceptado por instrucciones del usuario.

## Contexto

Se necesita iniciar un repositorio vacío a partir de un PDF, con una estructura similar al ejemplo de Betta Tech y operación entre Codex y Claude Code.

## Decisión

Usar reglas cortas en la raíz, perfiles especializados de Claude, specs oficiales, entregas e informes persistentes y un verificador ejecutable. Codex conserva la planificación y revisión; Claude implementa. GitHub Spec Kit se instala de verdad para ambos clientes y se versionan los archivos generados. No usar el líder constructor del ejemplo porque contradice la distribución pedida.

Git conserva la autoridad sobre requisitos y decisiones; NotebookLM es memoria consultable con referencias. Se eligió el servidor comunitario `notebooklm-mcp-cli`, fijado a 0.16.5, con autenticación local fuera de Git. No es una conexión oficial de Google ni una integración ya autenticada.

## Consecuencias

La recuperación de contexto no depende de la conversación. Los agentes requieren entregas explícitas y evidencia. El stack y despliegue de la aplicación quedan abiertos. Las instrucciones no impiden técnicamente que un cliente ignore su rol; la revisión y los checkpoints complementan las reglas. No se instala un sistema autónomo de ejecución entre clientes.
