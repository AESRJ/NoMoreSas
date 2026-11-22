# Modelo canónico004
Los límites siguientes son decisiones del prototipo, no mínimos oficiales. Proyecto/usuario/sesión de003 mantienen contratos.

## Profile
Una fila por proyecto; se borra en cascada con él. Escritura reemplaza perfil completo y genera nueva revisión si cambia contenido normalizado.
- `Profile.projectId`: UUID existente, propietario desde sesión, nunca de body.
- `Profile.cpuCores`: entero1–256.
- `Profile.ramGiB`: número finito0.5–4096.
- `Profile.storageGiB`: número finito1–100000, espacio libre declarado.
- `Profile.os`: linux/windows/macos/unknown.
- `Profile.architecture`: amd64/arm64/unknown.
- `Profile.storageKind`: ssd/hdd/network/unknown.
- `Profile.users`: entero1–10000.
- `Profile.dataGiB`: número finito0–100000, contenido esperado total.
- `Profile.access`: local/internet.
- `Profile.hasDomain`: booleano.
- `Profile.cpuFeaturesKnown`: booleano, solo declara si se comprobó x86-64-v2; falso implica pendiente para ML Immich amd64, no detección real.
- `Profile.revision`: entero positivo generado por servidor.

## Evaluation
- `Evaluation.status`: insufficient/pending/viable, siempre orientativo. Unknown, retiradas o condiciones no comprobadas impiden viable sin reservas; viable no garantía.
- `Evaluation.rulesVersion`: cadena estable versionada por servidor.
- `Evaluation.items`: desglose por alternativa con RAM/CPU editorial, datos oficiales separados, fuentes y fecha.
- `Evaluation.totals`: RAM, CPU y disco estimados; margen RAM25%, disco datos*1.25 + presupuestos base por servicio; CPU sumada, sin garantía de concurrencia. Mostrar ecuación y unidades. Reglas base editoriales: Nextcloud2GiB/2core/4GiB; Immich8/4/10; Synapse2/2/4; WireGuard0.25/1/0.25; Outline2/2/4. No mínimos oficiales. Carga >10 usuarios incrementa RAM/CPU por factor ceil(users/10), alcance declaradamente conservador; disco de datos se suma una sola vez. Advertir estimación no validada para carga alta.
- `Evaluation.warnings`: lista de códigos/texto/fuente; pendiente red/auth/arquitectura/CPUfeatures/servicio retirado; RAM/CPU/disco insuficientes prioritarios.

## Plan
- `Plan.fingerprint`: hash estable de projectId + alternativas ordenadas + perfil normalizado/revisión + rulesVersion + templatesVersion. Sin secretos.
- `Plan.steps`: IDs estables por alternativa y etapa, títulos, explicación, fuentes y prompt de plantilla. Cada servicio tiene preparación/instalación/verificación/recuperación; antes de copiar advierte campos pendientes. Pasos comunes opcionales con IDs deterministas.
- `Plan.blocked`: booleano si falta perfil, retirada o insuficiencia; contenido informativo visible, no fingir instalación apta. Condiciones pendientes visibles en prompts.

## Progress
- `Progress.projectId`: UUID, propietario desde sesión, FK cascade.
- `Progress.fingerprint`: debe coincidir con Plan.fingerprint actual o409.
- `Progress.completedStepIds`: array único, máximo100, solo IDs actuales; reemplazo atómico. Persistir solo datos necesarios y timestamps, no prompts/credenciales.
- `Progress.updatedAt`: ISO8601 generado por servidor.
Lectura con fingerprint diferente devuelve avance vacío y `stale:true`; escritura obsoleta409. Cambiar solo nombre/descripción no invalida plan; equipo/alternativas/reglas sí. Nunca borrar otros proyectos ni tablas anteriores.
