# Preparar «Continuar con Google»

Esto registra NoMoreSaaS ante Google; no es tu contraseña de Google. El código de006 ya incluye el botón «Continuar con Google» en /entrar y /registro y la vinculación desde «Mi cuenta», pero solo se activan cuando las tres variables de abajo están configuradas. Hasta entonces la aplicación muestra que Google no está disponible y sigue funcionando con correo y contraseña. El inicio de sesión real con Google aún no se ha probado: necesita completar estos pasos.

1. Entra en [Google Cloud Console](https://console.cloud.google.com/) con una cuenta que pueda administrar un proyecto. Usa un proyecto exclusivo de NoMoreSaaS.
2. Abre **Google Auth Platform** y completa la configuración de marca, audiencia y contacto que te solicite. Durante pruebas puede ser necesario agregar usuarios de prueba.
3. En **Clients**, crea un cliente de tipo **Web application**.
4. Registra como URI de retorno local `http://127.0.0.1:5573/api/auth/google/callback`. Debe coincidir exactamente con la dirección de la aplicación; no mezclar localhost y127.0.0.1.
5. Guarda Client ID y Client Secret solo en variables protegidas. No pegues la clave en el chat, Git, capturas o documentación.
6. Cuando Railway tenga su dominio estable, agrega también `https://DOMINIO/api/auth/google/callback` y configura ese mismo valor en el entorno de producción.
7. Prueba entrar, cancelar, cerrar sesión y vincular una cuenta local sin perder proyectos. Si el cliente sigue en modo de prueba, documenta quién puede utilizarlo; no declarar acceso público universal sin comprobar audiencia y consentimiento.

Variables, solo nombres (plantilla en `.env.example`):

```text
GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET
GOOGLE_REDIRECT_URI
```

- Se configuran las tres o ninguna. Con algunas vacías la API no arranca y lo indica por nombre de variable, sin mostrar valores.
- `GOOGLE_REDIRECT_URI` debe ser exactamente `APP_ORIGIN` seguido de `/api/auth/google/callback`. Con `APP_ORIGIN=http://127.0.0.1:5573` es la URI del paso4.
- Tras reiniciar la API, `/entrar` debe mostrar «Continuar con Google». Si sigue indicando que no está disponible, revisa las variables.

## Rutas y callbacks implementados

- `GET /api/auth/providers`: solo indica si Google está activo (`{google:{enabled}}`).
- `POST /api/auth/google/start`: inicia el acceso desde /entrar o /registro (CSRF y Origin).
- `POST /api/account/google/link/start`: inicia la vinculación desde «Mi cuenta». Pide la contraseña actual.
- `GET /api/account`: estado privado de la cuenta (tiene contraseña, Google activo o vinculado), sin identificadores de Google.
- `GET /api/auth/google/callback`: única URI de retorno registrada en Google. Siempre redirige con 303 a una ruta interna, nunca a una URL externa.
  - Acceso correcto: `/proyectos`. Vinculación correcta: `/cuenta?reason=google_linked`.
  - Errores: `reason=google_cancelled` (cancelado en Google), `google_failed` (intento vencido, repetido, de otra sesión o token no válido) y `google_conflict` (correo ya usado por una cuenta local, o Google ya vinculado a otra cuenta).
  - Los errores vuelven a `/entrar`; si el intento era de vinculación, a `/cuenta`. Nunca se muestran ni guardan códigos, tokens ni mensajes de Google.

Cada intento caduca a los 5 minutos, se usa una sola vez y queda ligado a la sesión del navegador que lo inició. Una coincidencia de correo nunca vincula cuentas: hay que entrar con contraseña y vincular desde «Mi cuenta».

## Estado de verificación (2026-11-22)

- Verificado sin Google real: pruebas de API con un cliente Google simulado, y la verificación de firma/emisor/audiencia/caducidad de `google-auth-library` con una clave local. En navegador (360 y 1280 px) se comprobó el estado sin configuración y el botón con respuestas simuladas, sin peticiones a Google.
- Pendiente: el acceso y la vinculación reales con Google. Requieren el cliente y el consentimiento de los pasos1–6 y probar el paso7. Hasta entonces esta función no debe darse por terminada.

Se conservará el acceso por correo/contraseña. Google no requiere dar acceso a Drive, Gmail o tus archivos para identificarte. El flujo elegido es de servidor; no necesita añadir un SDK Google al frontend.

Fuentes: [Google OIDC](https://developers.google.com/identity/openid-connect/openid-connect), [flujo para servidor web](https://developers.google.com/identity/protocols/oauth2/web-server).
