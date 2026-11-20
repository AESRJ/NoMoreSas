# Verificación

```powershell
.\init.cmd
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
git diff --check
.\.venv\Scripts\specify.exe integration list
.\.venv\Scripts\python.exe -m pip check
```

El verificador usa solo la biblioteca estándar de Python: comprueba archivos clave, integraciones, perfiles, referencias a specs, IDs únicos, estados y límite de una funcionalidad activa. Para entregar a Claude, su modo `--implementation-ready` exige entrega de Codex, feature activa, spec/plan/tasks existentes, tareas pendientes identificadas y comandos de aceptación definidos.

Si PowerShell bloquea scripts, `init.cmd` ejecuta `init.ps1` con política acotada al proceso. Para los scripts oficiales de Spec Kit se puede usar `powershell -NoProfile -ExecutionPolicy Bypass -File <ruta.ps1> <argumentos>`; no cambiar la política global. `init.ps1` sigue siendo válido cuando la política permite ejecutarlo directamente.

Los avisos de CLI ausente no equivalen a un fallo estructural. Una autenticación válida de NotebookLM y una consulta con fuentes son necesarias para declarar la integración operativa; tener el ejecutable y la configuración no lo demuestra.

CI valida el arnés y formato de diff en Windows. No necesita Google ni secretos. Los checks de aplicación se agregarán al elegir el stack y escribir el primer plan; por ahora no existen tests ni código del producto. Los comandos de aceptación de cada entrega deben ejecutar esas pruebas reales y registrar su resultado.
