# ADR 0003: separar el repositorio del código de aplicación

Fecha: 2026-11-20. Estado: aceptado por instrucción explícita del usuario.

El usuario solicita publicar el avance actual y que el código del producto se encuentre en otro repositorio. AESRJ/NoMoreSas conserva el arnés, documentación, fuente original y planificación SDD. No se inicia implementación de React/Vite/Express aquí.

El nombre, URL y visibilidad del repositorio de aplicación todavía no están definidos. No se crea un destino por inferencia. Antes de construir, Codex debe adaptar las reglas, especificaciones, rutas y verificaciones al repositorio acordado, dejar claras las fuentes de autoridad de cada artefacto y preparar una entrega validada para Claude.

La entrega 002 cambia de ready a blocked y el índice refleja la dependencia. Las rutas apps/web y apps/api del plan describen la estructura prevista dentro del futuro repositorio de código, no una autorización de creación en este repositorio. Se conserva el diseño sin duplicar ni mover archivos todavía.

Esta instrucción autoriza el push del avance actual. No autoriza empezar la construcción, publicar una aplicación ni crear un repositorio sin concretar su destino.
