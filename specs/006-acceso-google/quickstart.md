# Quickstart / validación 006-acceso-google
Encheckout C:/Users/Roel/Documents/NoMoreSaaS_Frontend, Node26.13.1/pnpm12.21.0, init.cmd y entrega actualready. Sólo ejecutar tarea solicitada y dependenciasaceptadas. pnpm install --frozen-lockfile si cambia lockfile; .env/DBlocalpreservados.
1. Ejecutar escenariosUS y SC de spec.md con datosválidos y casoerror/privacidad pertinente; registrar observables.
2. Verificar tareas con pruebas existentes afectadas y nuevas solo cuandoprueban riesgo real. pnpm lint y pnpm build alintegrar.
3. Navegador con API/DBtemporal a360/1280; variablesAPI_PORT3501 yWEB_PORT5773 establecidas antesdepnpm; no utilizar previewactual. No fixtures deéxito que oculten integración real.
4. Datos/secretosnunca enGit/logs/capturas ni memoria externa. Google/Railway/configuración real se verifican separadamente; no marcarpruebaviva aprobada por mocks o conexiónsupuestamentehecha.
5. Evidencia breve .project/progress/impl_AUTH-GOOGLE.md y revisión Codex. Cerrarsoloal cumplirFR/SC, checks y dependenciasexternas; constructor no cierra.
Aceptación particular: SC-001 CuentaGoogle inicia sesión y accede solo a sus proyectos; logout revoca sesión. SC-002 Cuenta local existente conserva acceso/proyectos y puede vincularGoogle tras reautenticación; mismoemail por sísolo no concede acceso. SC-003 Callback inválido/vencido/repetido/cambiado no crea sesión ni vínculo; configuración ausente se comunica sin botónfalso.
