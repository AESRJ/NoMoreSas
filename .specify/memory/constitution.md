# Constitución de NoMoreSaaS

Versión: 1.0.0. Ratificada: 2026-11-19. Última modificación: 2026-11-19.

## I. Especificar antes de construir

Cada incremento debe tener spec, plan, tareas y criterios observables. No implementar producto con dudas que afecten al alcance. Las posibilidades del PDF no son compromisos automáticos; conservar trazabilidad hacia páginas, decisiones y tareas.

## II. Responsabilidades estables

Codex planifica y revisa; Claude Code implementa. El usuario controla prioridades y decisiones de producto. Codex puede construir y mantener la infraestructura del arnés autorizada, pero no el producto. Un constructor no aprueba su propio trabajo. Toda corrección de código de producto vuelve a Claude.

## III. Datos y fuentes comprobables

Respetar el control de datos que motiva el proyecto. No guardar secretos en Git ni enviarlos a la memoria. Catálogo y estimaciones deben distinguir fuentes, fechas, supuestos, incertidumbre y compatibilidad. No presentar cifras de ejemplo como garantías.

## IV. Cambios acotados y reversibles

Una funcionalidad activa a la vez. No incorporar SSH ni ejecución de instalaciones en el MVP sin nueva especificación y autorización del usuario. Definir estrategia de reversión cuando haya migraciones. Elegir la estructura más simple que cumpla el alcance acordado.

## V. Evidencia y contexto persistente

Registrar decisiones, archivos afectados y resultados reales de verificación. Actualizar estado y bitácora en cada sesión. Git es la fuente de autoridad; NotebookLM es una memoria auxiliar con citas verificables. Si la memoria externa falla, registrar la limitación y continuar con las fuentes locales.

## Calidad y cierre

Las pruebas se eligen según el riesgo del cambio: aceptación, lógica, integración, privacidad y accesibilidad según corresponda. El verificador del arnés no sustituye pruebas del producto. Una feature solo es done con criterios cumplidos, evidencia y revisión independiente, de acuerdo con CHECKPOINTS.md.

## Gobierno

Modificar principios requiere una decisión registrada con motivo, impacto y versión. Las instrucciones explícitas del usuario prevalecen. Los skills oficiales de Spec Kit se usan dentro de esta distribución de responsabilidades, aunque incluyan comandos para otros roles. Las instrucciones son reglas de operación, no barreras técnicas de seguridad.
