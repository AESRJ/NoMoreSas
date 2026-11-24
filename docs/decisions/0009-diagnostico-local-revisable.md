> Nota vigente23-11-2026: documento histórico; Google y/o recopilador/importación fueron retirados del producto. Ver ADR0011 y docs/reviews/2026-11-23-cambios-claude.md. No usarlo como autorización de implementación.

# ADR 0009: diagnóstico revisable y opción manual

Fecha: 2026-11-22. Propuesta técnica definida dentro del alcance solicitado.

El navegador no proporciona un inventario completo fiable. Ofrecer ayuda parcial etiquetada, importación de diagnóstico local y formulario manual, que el usuario confirmó conservar.

Primer recopilador: Windows 10/11 con Node 22 o superior. Solo lectura del sistema y consultas CIM fijas, sin administrador, red, agente persistente o cambios de configuración. Su único archivo de salida es el JSON de diagnóstico solicitado; no sobrescribe un archivo existente. No se ejecuta automáticamente en el equipo del desarrollador.

El usuario confirma el equipo destino y revisa los datos antes de guardarlos. Excluir identificadores y secretos. Validar importación como dato no confiable, conservar origen/precisión por campo y no convertir cuota web en disco libre. Los demás sistemas conservan manual/importación; no prometer un recopilador multiplataforma sin construirlo. Detalle y límites en007.
