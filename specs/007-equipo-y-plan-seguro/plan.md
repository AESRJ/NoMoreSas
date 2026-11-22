# Implementation Plan: Equipo asistido y prompts claros con seguridad
**Branch**:feat/revision-y-railway | **Date**:2026-11-22 | **Spec**:spec.md

## Summary
Construir solo alcance especificado, por Claude una tarea por invocación; revisión/commits por Codex. Dependencias: UX-REVISION code reviewed, AUTH-GOOGLE migration003 code reviewed.

## Technical Context
Stack existenteReact/Vite/Router/Zustand/pnpm, JS ESM, Express/SQLite/Argon2nativo Node26. No Next/Django/ORM ni cambiosglobales de herramientas.

## Constitution Check
PASS: especificaciónprevia, rolesestables, fuentes/supuestos, unaactiva, migración/reversión explícita si aplica, evidenciareal. Despliegue sólo aplicación008 pedido expresamente, no instalaciónremota de serviciosusuarios niSSH.

## Design & Project Structure
Primer recopilador para Windows10/11, decisión de alcance inicial basada en entornoactual delusuario; no prometer soporteLinux/macOSautomático aún, manual/importación deesquema validado siguen disponibles. Node22+ para herramienta local deexportación, no requierePython/agenteinstalado/admin. Archivo descargable .mjs revisable, comando node nomoresaas-diagnostico.mjs --output equipo.json; usa os y consultaCIM por PowerShell -NoProfile -NonInteractive con comandosfijos/timeout, sin interpolarentrada delusuario ni ExecutionPolicyBypass, sin red/instalaciones. SoloescribeJSONsolicitado con UTF8yflagwx; siarchivoexistefalla sin sobrescribirlo. No ejecutarlo automáticamente en máquina deldesarrollador: fixtures y sistemas de pruebaautorizados, usuario final lo ejecuta voluntariamente enequipo destino.
DatosCIM seleccionados: CPUmodelo, núcleos físicos/lógicos separados, RAMtotal, SO/arquitectura y discoslocalesFreeSpace/Size. No pedirpropiedadesdeserializadas completas (hostname/serial/MAC/usuarios/rutaspersonales). Volúmenes se etiquetan poríndice enexport, userselecciona unoalimportar; storageKindunknown si no puedeprobarseSSD/HDD. GPU solo nombre opcional informativo, no usarmemoriaGPU ni declararcompatibilidadML inventada. CPUfeaturesx86v2unknown salvocomprobación real; no derivarla demarcaCPU.
Browser: hardwareConcurrency se muestra como hilos disponiblesaproximados, no núcleosfísicos exactos. deviceMemory esoptativo/inexacto/no universal, no dependencia. No usar storage.estimate paraProfile.storageGiB. Mostrar datos parciales aparte; confirmación delusuario antes de usar aproximación como declarada. Campo no comprobado generaadvertencia pendiente incluso aunque presupuesto quepa. Detección no recopilaIP/identificadores ni manda nada a terceros.
ImportarJSON≤64KiB, allowlistesquema1, número finito y unidadesbytes. Convertir aGiBsinconfundirGB, permitirselecciónvolumen y guardar trasvista previa. Arq/osincorrectos o campossinprueba permanecen desconocidos. Mantener formulariomanual actual y requerimientos numéricos; entrada fuera delrango deperfil produceerror, no truncar. Metadatos porcampo y timestamps en tablaaditiva004-profile-provenance.sql tras006003. LaAPI mantieneproyectosowner/CSRF y revisionperfil; canonicalguardarperfil puedeaceptar provenanceopcional, ausente→manual paraantiguosclientes/perfiles. Cambios numéricos/procedencia que afectancertidumbre incrementanrevision e invalidanplan; no esconder ediciones manuales previas.
EvaluationView: resumen estado+3indicadores+motivos/siguienteacción, detalle técnico/fuentes en disclosure. No garantizarcomponentes detectados ni hardwaremínimo certificado. Plan versiontemplates+rules almodificartextos/invalidation, no reutilizaravances de versiónanterior.
Prompts: Objetivo, Contexto relevante, Antes de empezar(readonly), Acciones propuestas, Seguridad, Cómo comprobar, Cómo volver atrás. Controles de permisosmínimos, claves locales/variablesplaceholder, noexponerDBRedisPostgres, puertos necesarios/TLS, datos/volúmenes, backup/restore, versiones oficiales y recuperación. Solo relevantes a lafase; WireGuardnativo y condicionesNAT/keys propias, noforzarDocker. No ejecutarinstalaciones/SSH ni generarcomandosdestructivosautomáticos. No expandir bloqueo de todo elplan poravisoinformativo: condicionescriticas sí requierenresolverantes deinstalar.

## Phase0 Research / Phase1 Design
research.md, data-model.md, contracts/contract.md y quickstart.md. Fuentesprimarias; no pendiente de decisiones técnicas sin alternativa razonable. Activaciónserial segúncola; códigoaprobado convalidaciónexterna faltante se indica in_review/blocked, no done.

## Verification / rollback
Ver quickstart.md y tareas por riesgo. Pruebas enfocadas por tarea, lint/build y smoke final360/1280; no repetición masiva por cambiosdocumentales. DBs/puertos temporales3501/5773 o3351/5583, no preview3301/5573. Copia consistente antes de migrar DBreal, noreset/clean/dropdatos. Revertir app mediante commits revisados; restauración/migración sólo concompatibilidad comprobada, nuncadowngrade destructivo silencioso.

## Complexity Tracking
Solo dependencias y tablasjustificadas; detalles delalcance/valores de modelo canónicos se citan desde tasks. Documentar asistencia/comandos brevemente, sinrazonamiento interno ni secretos.
