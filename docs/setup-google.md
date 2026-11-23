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

Se conservará el acceso por correo/contraseña. Google no requiere dar acceso a Drive, Gmail o tus archivos para identificarte. El flujo elegido es de servidor; no necesita añadir un SDK Google al frontend.

Fuentes: [Google OIDC](https://developers.google.com/identity/openid-connect/openid-connect), [flujo para servidor web](https://developers.google.com/identity/protocols/oauth2/web-server).
