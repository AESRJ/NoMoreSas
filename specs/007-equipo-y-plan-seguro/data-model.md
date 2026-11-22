## Diagnostic (nuevo, no confiable)
- `Diagnostic.schemaVersion`: literal1.
- `Diagnostic.capturedAt`: ISOválido, no másde5min enfuturo; antiguos>30d permiten revisar con aviso, no implican actual.
- `Diagnostic.os`: windows|linux|macos|unknown; recopiladorinicial soloWindows, otros importesno certifican soporte de herramienta.
- `Diagnostic.architecture`: amd64|arm64|unknown.
- `Diagnostic.cpu`: {model?:texto≤200,physicalCores?:entero1–256,logicalThreads?:entero1–1024}; faltantequedaunknown, logicalnoequivalephysical.
- `Diagnostic.ramBytes`: enterofinito positivo≤MAX_SAFE_INTEGER o null.
- `Diagnostic.volumes`: array0–32 de {label:Volume N,freeBytes,sizeBytes}; bytesenterosfinitos0≤free≤size≤MAX_SAFE_INTEGER, sinrutas/seriales.
- `Diagnostic.gpuNames`: opcionalarray0–8 detextos≤200; solo informativo.
Rechazar campos extra, anidamientos inesperados/tamañomayor64KiB. Noevaluar strings/rutas/URLs/comandos. Conversiónvalidada aloslímitesProfile003/004, no truncar.
## ProfileProvenance
- `ProfileProvenance.projectId`: UUIDPK/FKprojectCascade/ownerde sesión.
- `ProfileProvenance.target`: this-device|other-device, confirmado porusuario.
- `ProfileProvenance.fields`: mapa solo camposeditablesProfile→{source:manual|browser|import,certainty:declared|approximate|reported,capturedAt:ISO|null}; manualaleditarelcampo. Sin credenciales/serial/hostname/rutas.
- `ProfileProvenance.collectorVersion`: nullotexto≤40; informativo, noatestación.
CamposProfile/límites004seconservan; metadatosausentes→manual/declared. Aproximación nopermite resultado viable sinreservas. Hashplanincluyerevision y versionesreglas/templates, persisteowner003.
