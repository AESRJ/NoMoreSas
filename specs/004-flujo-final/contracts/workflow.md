# Contrato privado004
Reutilizar middleware auth, CSRF/Origin y parser limitado existentes. Todas las rutas bajo /api/projects/:id; SQL une ID y ownerId de sesión. Ajeno/inexistente404 indistinguibles; sin sesión401. Mutación con CSRF/Origin inválidos403; perfil inválido400 con campos; cuerpo excesivo413/tipo415; no-store. Ignorar ningún campo extra: rechazarlo. Respuestas no contienen credenciales ni datos de otro usuario.

- GET /api/projects/:id/workflow →200 {profile:null|Profile,evaluation:null|Evaluation,plan:null|Plan,progress:{completedStepIds:[],stale:boolean,updatedAt:null|ISO}}. Proyecto sin perfil es estado vacío normal, sin plan apto.
- PUT /api/projects/:id/profile →200 mismo documento workflow tras validar Profile (solo campos editables; rechazar projectId/revision/ownerId). Crear/upsert y recalcular. Sin cambios normalizados conserva revisión.
- PUT /api/projects/:id/progress body {fingerprint,completedStepIds} →200 {fingerprint,completedStepIds,updatedAt}; obsoleto409, IDpaso ajeno400. Guardar atómicamente, leer versión actual dentro de transacción.
- Catálogo público conserva su forma salvo seed y nueva clasificación de licencia si necesaria. No crear una relación SaaS falsa para conservar antiguo validador de cobertura.

UI: ruta privada /proyectos/:id/flujo con navegación Equipo/Evaluación/Plan. Enlace desde detalle de proyecto y retorno claro. Estado privado en memoria, invalidar por cambio de usuario; abortar respuestas obsoletas con patrones003. Guardado explícito del perfil. Cambios de perfil/selección con avance previo avisan que se recalculará; avance nuevo no hereda checkboxes. Prompts con nombres de campos y valores escapados como contenido, sin HTML inyectado, sin ejecuciones. Portapapeles usa writeText con fallback de texto seleccionable.

Licencia: si Outline necesita source-available, ampliar validación/UI de forma compatible con entradas anteriores. Mensajes del sitio deben decir alternativas autoalojadas, no asegurar que todas son open source.
