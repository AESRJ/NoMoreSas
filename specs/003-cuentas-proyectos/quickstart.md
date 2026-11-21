# Verificación de cuentas y proyectos

En checkout NoMoreSaaS_Frontend con Node26.13.1 y pnpm12.21.0:

1. pnpm install --frozen-lockfile. Copiar .env.example a configuración local ignorada conforme instrucciones que Claude implemente; generar SESSION_SECRET criptográfico mínimo32bytes. Definir DATABASE_PATH, APP_ORIGIN=http://127.0.0.1:5173 y modo cookie de desarrollo loopback. No subir secreto/DB a Git.
2. pnpm db:migrate aplica migraciones idempotentes sobre DB configurada; código de salida0. Ruta inaccesible/configuración inválida: fallo claro, sin memoria de sustitución. pnpm dev sirve API loopback3001 y Vite5173 con proxy /api.
3. Registrar usuarioA, crear dos proyectos, editar uno, salir/entrar y comprobar persistencia. Reiniciar API: cuenta, proyectos y sesión válida se conservan.
4. UsuarioB en contexto separado: no ve proyectosA, y copiar UUID de A no permite lectura/edición/borrado. Verificar A intacto. Cerrar sesión invalida cookie vieja. Cancelar borrado no altera nada y confirmar elimina solo proyecto propio.
5. pnpm lint; pnpm test; pnpm build; pnpm test:e2e; init.cmd. Cada código debe ser0 al cerrar; se conserva cobertura de catálogo. Las pruebas de auth/DB usan temporales, nunca DATABASE_PATH real. Playwright usa DB/secret propios y aísla identidades/contextos; prueba reinicio en integración API con archivo temporal.
6. Simular expiración con reloj inyectado y un intento CSRF/origen ajeno: rechazo observable. No esperar treinta minutos en una prueba. No afirmar auditoría de seguridad completa o aptitud productiva.

Guardar por tarea evidencia breve en .project/progress/impl_MVP-IDENTIDAD.md (archivos, comandos y resultados), y Codex revisa antes del commit. No versionar capturas/credenciales/datos de usuarios.
