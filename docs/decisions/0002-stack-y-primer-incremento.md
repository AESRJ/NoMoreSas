# ADR 0002: frontend de clase, Express y primer incremento

Fecha: 2026-11-20. Estado: aceptado por confirmación explícita del usuario en esta sesión.

## Contexto

El usuario necesita emplear las tecnologías de clase. El PDF describe el producto y ejemplos de servicios autoalojados; las elecciones siguientes se confirmaron directamente en la conversación y no se atribuyen al PDF.

## Decisiones confirmadas

- Frontend: React, React Router, Zustand y gestor pnpm.
- Backend: Node.js con Express, elegido por el usuario tras comparar Express, NestJS y FastAPI.
- Primer incremento: catálogo público, búsqueda, fichas y comparación. Cuentas, proyectos, hardware y prompts permanecen en el backlog.
- Codex planifica y revisa; Claude Code construye.

## Propuestas descartadas

La propuesta inicial de Django fue retirada al aclararse los requisitos de clase. No se instaló Django ni se escribió implementación con él. Next.js no es un requisito y no se incorpora como framework adicional.

## Consecuencias para el plan

Planificar una SPA React con una API Express, paquetes gestionados por pnpm y almacenamiento de estado de selección en Zustand. React Router gestiona la navegación. Como elección de implementación de Codex, iniciar con JavaScript y Vite, sin exigir TypeScript ni un framework adicional; documentar esa elección y sus riesgos en research.md.

El catálogo inicial puede ser un archivo curado versionado servido por la API, sin introducir una base de datos ni autenticación antes de necesitarlas. Esta es una decisión acotada al primer incremento; la persistencia de proyectos y usuarios requiere una nueva revisión antes de implementarla. No usar JSON como persistencia concurrente de cuentas.

## Fuentes para la evaluación

- [React: crear una aplicación desde cero](https://react.dev/learn/build-a-react-app-from-scratch).
- [Express](https://expressjs.com/), [NestJS](https://docs.nestjs.com/) y [FastAPI](https://fastapi.tiangolo.com/).
- [Instalación pnpm](https://pnpm.io/installation).
