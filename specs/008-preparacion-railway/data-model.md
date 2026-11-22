## RuntimeConfig
- `RuntimeConfig.mode`: development|production, sólo production activa estáticos/port/proxypolicy.
- `RuntimeConfig.port`: entero1–65535 desde PORTprod, sinpuerto fijo deVite; API_PORT desarrollo se conserva.
- `RuntimeConfig.host`:0.0.0.0producción,loopbackdev.
- `RuntimeConfig.appOrigin`: origenexactoHTTPSprod, sinpaths/trailing slash; no inferirHost.
- `RuntimeConfig.trustedProxyHops`:enteroacotado0–2 con defaultdev0; productionvalorvalidado contra ingressreal, no true.
- `RuntimeConfig.databasePath`: rutaabsoluta /data/nomoresaas/production.sqlite, fueraestáticos; perduraenvolumen.
- `RuntimeConfig.sessionSecret`:≥32bytesaleatoriosestable sólosecretoServidor; no frontend/logs/Git.
- `RuntimeConfig.googleClientId`: identificador OAuth público, configurado solo en servidor según006.
- `RuntimeConfig.googleClientSecret`: secreto OAuth solo servidor, nunca bundle/log/Git.
- `RuntimeConfig.googleRedirectUri`: URL HTTPS exacta del callback, en el mismo APP_ORIGIN, registrada en Google.
## ReleaseRecord
- `ReleaseRecord.commit`: SHA40revisado, no workingtreearbitrario.
- `ReleaseRecord.serviceId/environmentId/domain`: IDs/origenreal verificadopostconexion; desconocidos no se inventan.
- `ReleaseRecord.replicaCount`:literal1conSQLitevolumen.
- `ReleaseRecord.volumeMount`:literal/data;capacidad inicial≤planreal.
- `ReleaseRecord.backupReference`:referenciano secreta/fecha/hash debackupconsistente o ausente paraDBnuevavacía; nunca contenidoSQL.
- `ReleaseRecord.deploymentStatus`:prepared|blocked|deploying|verified|failed, verifiedsoloSHA+URL+smoke+persistenciacomprobados.
- `ReleaseRecord.spendLimit`:nullhastaaprobar gasto segúncuenta; nullnoautoriza upgrades, cobrarcompra o prometergratuidad.
Estas sonconfiguraciones/registrooperativo, no entidadde negocio ni tabla adicionalpornecesidad.
