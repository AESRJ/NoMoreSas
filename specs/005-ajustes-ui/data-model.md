## Service (extensión compatible)
- `Service.id`, `Service.name`, `Service.description`: contratos existentes sin cambiar identificadores.
- `Service.officialUrl`: opcional, URLHTTPS oficial; si existe se valida. Seed actualizado con fuente real, fixtures anteriores sin ella siguen válidos.
- `Service.sources`: opcional, array1–8 de {urlHTTPS,checkedAt fechaISO nofutura,kind:official,note:texto1–1000}. No ejecutar ni renderHTML. Si falta, datos no disponibles para esa comparación se indican desconocidos.
## ExplorerState
- `ExplorerState.activeServiceId`: null o IDdeService vigente.
- `ExplorerState.activeAlternativeId`: null o IDrelacionado con activeServiceId. Cambio de servicio borra alternativa activa incompatible.
- `ExplorerState.query`: texto de búsqueda como contrato actual, sin modificar semántica de coincidencia ni exponer estado privado.
## ProjectSelection
- `ProjectSelection.alternativeIds`:1–10 IDs únicos actuales, límites003. Retirados en edición permanecen visibles hasta que el usuario los sustituya, no se envían como nuevos seleccionables. Sin nuevos owners ni datos fuera de sesión.
