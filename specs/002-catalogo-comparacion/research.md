# Investigación y decisiones del incremento

Fecha: 2026-11-20. Codex planificador; investigación auxiliar requerida por speckit-plan, sin construcción ni edición de producto.

| Decisión | Motivo | Alternativas consideradas y fuentes |
| --- | --- | --- |
| React + Router declarativo + Zustand + pnpm | Restricciones de clase confirmadas por el usuario | No sustituir por Next.js. [React](https://react.dev/learn/build-a-react-app-from-scratch), [Router](https://reactrouter.com/start/declarative/installation), [Zustand](https://github.com/pmndrs/zustand), [pnpm](https://pnpm.io/installation) |
| Vite con JavaScript | SPA acotada y alineada con clase; no introducir TypeScript sin necesidad | Modo framework y SSR no requeridos. [Guía Vite](https://vite.dev/guide/) |
| Express 5 | Elegido por el usuario entre Express, NestJS y FastAPI | [Express API](https://expressjs.com/en/5x/api/), [NestJS](https://docs.nestjs.com/), [FastAPI](https://fastapi.tiangolo.com/) |
| Dataset curado versionado detrás de API | Pequeño, de lectura y auditable; permite aprender integración real | DB y ORM se revisan al trabajar cuentas/proyectos, no ahora |
| Selección en Zustand, búsqueda en URL, catálogo en caché del cliente | Delimitar estado UI, navegación y datos remotos sin duplicación | Zustand puede hacer tareas asíncronas; no es una limitación de la biblioteca. [URL values](https://reactrouter.com/start/declarative/url-values) |
| Pruebas por capas | Demostrar contratos, interacción y recorrido real con errores | [Vitest](https://vitest.dev/guide/), [Testing Library](https://testing-library.com/docs/react-testing-library/intro/), [Supertest](https://github.com/forwardemail/supertest), [Playwright](https://playwright.dev/docs/intro) |
| Errores centrales y sin stacks públicos | Evitar filtraciones y estados ambiguos | [Errores Express](https://expressjs.com/en/guide/error-handling/), [seguridad](https://expressjs.com/en/advanced/best-practice-security/) |

## Compatibilidad y fijación

Node LTS 26.13.1 instalado por WinGet y comprobado. La instalación de pnpm se registra con su versión efectiva en la bitácora. Al construir, Claude verificará los `engines` y peer dependencies de sus versiones concretas, fijará `packageManager` con la versión instalada, dependencias directas exactas y lockfile. No se presupone que una etiqueta latest futura sea compatible.

La documentación consultada de Express 5 exige Node >=18; Vite indica como mínimos 20.19+ o 22.12+ y advierte que algunas plantillas exigen más. El runtime instalado supera esos mínimos; eso no sustituye la comprobación de versiones concretas al crear los paquetes.

## Riesgos y tratamiento

- Licencias y capacidades cambian: fuente y fecha por dato; no equiparar source-available con open source.
- El catálogo inicial necesita al menos dos alternativas comparables para un SaaS: seed y pruebas deben verificarlo.
- Búsqueda vacía, error API y cero registros son estados diferentes. No devolver datos vacíos como fallback de errores.
- Enlaces de rutas deben funcionar al recargar el servidor local; probarlo con navegador real.
- Sin DB ni cuentas no se valida persistencia de proyectos: queda fuera de este incremento y no se anuncia como implementada.
- Cuatro dependencias de pruebas no habilitan todas las clases de verificación automáticamente: registrar qué se ejecutó, con resultados y límites.
