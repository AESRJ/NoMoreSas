# Implementation Plan: Exploración por servicio y revisión de interfaz
**Branch**:feat/revision-y-railway | **Date**:2026-11-22 | **Spec**:spec.md

## Summary
Construir solo alcance especificado, por Claude una tarea por invocación; revisión/commits por Codex. Dependencias: 004 cerrado.

## Technical Context
Stack existenteReact/Vite/Router/Zustand/pnpm, JS ESM, Express/SQLite/Argon2nativo Node26. No Next/Django/ORM ni cambiosglobales de herramientas.

## Constitution Check
PASS: especificaciónprevia, rolesestables, fuentes/supuestos, unaactiva, migración/reversión explícita si aplica, evidenciareal. Despliegue sólo aplicación008 pedido expresamente, no instalaciónremota de serviciosusuarios niSSH.

## Design & Project Structure
Reutilizar ReactRouter/Zustand/componentes/catalog-index y API existentes. Publicar ServiceExplorer con botones circulares semánticos, árbol DOM y un panel de comparación dentro de CatalogPage. Estado activo ligado a pares válidos del catálogo; animación CSS con prefers-reduced-motion. No generar gráficas pesadas ni usar canvas para controles interactivos. Desmontar interfaz global antigua de comparación; /comparar redirige al catálogo con aviso/enlace, conservando fichas/URLsdealternativas y datos privados. No mantener dos experiencias visibles de comparar.
Extraer selector de proyecto ServiceReplacementPicker que reutilice relaciones y búsqueda: elegir servicio, mostrar reemplazos, guardar solo alternativeIds actuales bajo contrato003. Etiquetas visibles servicio→alternativa, sin duplicados; retiradas siguen visibles con posibilidad de reemplazo, no eliminación silenciosa. Errores/red/401 preservan valores y aislamiento003.
Comparación publica solo atributos verificables: descripción, capacidades/diferencias y responsabilidades de alojamiento/mantenimiento con fuentes oficiales; datosSaaS desconocidos se muestran como tales. Ampliar metadatos opcionales deService para fuentes/URL, manteniendo schemaVersion1 y fixtures viejos válidos. No inventar precios ni tabla de paridad. Claude verifica páginas oficiales al curar esas comparaciones.
Textos: título «Tus servicios. Tus reglas.», bajada «Elige lo que usas. Encuentra su reemplazo.», label «Encuentra una alternativa», placeholder «Por ejemplo, Google Drive», ayuda «Escribe el nombre del servicio que quieres reemplazar». Password: ayuda «Usa una frase de al menos 15 caracteres»; máximo128 solo en error al excederlo, sin trim/truncado ni complejidad nueva. Son decisiones de copy de Codex dentro del feedback, revisables por usuario.
Foco, anuncios de expansión y jerarquía de headings; no invocar comparativa por hover solamente. Impeccable existente para diseño, sinPRODUCT/DESIGN. No nueva imagen ni créditosHiggsfield. UI cambia dentro de apps/web; catálogo/validador y pruebas deAPI solo para metadatosService verificables. Sin otra arquitectura.

## Phase0 Research / Phase1 Design
research.md, data-model.md, contracts/contract.md y quickstart.md. Fuentesprimarias; no pendiente de decisiones técnicas sin alternativa razonable. Activaciónserial segúncola; códigoaprobado convalidaciónexterna faltante se indica in_review/blocked, no done.

## Verification / rollback
Ver quickstart.md y tareas por riesgo. Pruebas enfocadas por tarea, lint/build y smoke final360/1280; no repetición masiva por cambiosdocumentales. DBs/puertos temporales3501/5773 o3351/5583, no preview3301/5573. Copia consistente antes de migrar DBreal, noreset/clean/dropdatos. Revertir app mediante commits revisados; restauración/migración sólo concompatibilidad comprobada, nuncadowngrade destructivo silencioso.

## Complexity Tracking
Solo dependencias y tablasjustificadas; detalles delalcance/valores de modelo canónicos se citan desde tasks. Documentar asistencia/comandos brevemente, sinrazonamiento interno ni secretos.

## Ajuste de verificación T004 — 2026-11-22
API263/263PASS sin paralelismo y db28/28PASS aislado; pnpm test paralelo repite timeout5s creando100proyectos con commitsSQLiteFULL individuales. Autorizar solo estabilizar preparación de fixtures de esa prueba en apps/api/tests/db.test.js, manteniendo límite100, rechazo101, segunda cuenta y aserciones. Claude decide implementación mínima; no aumentar límites/timeout global ni cambiar producto/DBreal. RevisiónCodex antes de aceptar, pnpm test integradoPASS requerido.
