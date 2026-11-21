# Guía de implementación y comprobación

Los comandos de aplicación son el contrato que Claude debe construir; hoy todavía no hay paquetes de aplicación.

## Prerrequisitos

Node LTS, pnpm y Git; abrir una terminal nueva después de instalar para recoger el PATH. Usar `pnpm.cmd` en PowerShell si la política bloquea `pnpm.ps1`. Codex y Claude Code autenticados según su propia configuración; el acceso a NotebookLM no autoriza cambios de producto.

## Puerta de entrada para Claude

```powershell
.\init.cmd
.\.venv\Scripts\python.exe scripts/check_harness.py --implementation-ready handoffs/002-catalogo-comparacion.json
```

Leer `CLAUDE.md`, la entrega y todos los artefactos de esta especificación antes de ejecutar `/speckit-implement`. No iniciar si la puerta falla.

## Preparación que debe dejar reproducible

```powershell
pnpm install --frozen-lockfile
pnpm dev
```

En la primera construcción no existe lockfile: Claude instala versiones compatibles con `pnpm install`, fija `packageManager` y dependencias y guarda el lockfile. A partir de ese momento la reproducción usa `--frozen-lockfile`. No repetir bootstrap de Spec Kit ni borrar las reglas.

Visitar `http://127.0.0.1:5173`; la API atiende en 3001 y Vite hace proxy de `/api`. Ningún proceso se expone a red externa por defecto.

## Comprobación automatizada

```powershell
pnpm lint
pnpm test
pnpm build
pnpm exec playwright install chromium
pnpm test:e2e
.\init.cmd
```

`test:e2e` debe iniciar y cerrar servidores locales mediante configuración de Playwright. Si faltan descargas o permisos, registrar el prerrequisito real; no marcar prueba superada. El arnés Python y la aplicación tienen pruebas independientes.

## Aceptación manual

1. Entrar sin cuenta: al menos tres SaaS y cuatro alternativas curadas.
2. Buscar un SaaS con mayúsculas/espacios; verificar el filtro. Buscar un nombre inexistente y restablecer.
3. Abrir una ficha mediante navegación y enlace directo; recargar y comprobar fuentes y fecha.
4. Agregar, quitar y limpiar alternativas. Repetir una selección y superar tres; no debe duplicar ni exceder el límite.
5. Comparar dos opciones relacionadas y dos de distintas necesidades; comprobar criterios alineados y aviso correspondiente.
6. Probar carga, error con reintento, vacío y recurso no encontrado mediante fixtures/mocks de pruebas; no modificar el seed real para simular resultados.
7. Repetir el recorrido solo con teclado y en 360/1280 px. Documentar capturas y límites observados.

Claude registra tareas, archivos, comandos y códigos de salida en `progress/impl_MVP-CATALOGO.md`. Codex revisa después en `progress/review_MVP-CATALOGO.md`; no cerrar la feature por tener el plan preparado.
