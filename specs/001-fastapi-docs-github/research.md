# Phase 0: Research & Discovery

This document outlines the decisions made to resolve ambiguities found in the initial feature specification and technical context.

## 1. Performance Goals

- **Decision**: For the initial version, we will target a non-functional requirement of **Largest Contentful Paint (LCP) under 2.5 seconds** for all tutorial pages on a standard broadband connection.
- **Rationale**: As a content-focused site, fast page loads are critical for user experience. LCP is a standard Core Web Vital metric that aligns with this goal.
- **Alternatives considered**: Time to First Byte (TTFB) was considered but is less user-centric. A full suite of performance metrics is overkill for the initial MVP.

## 2. FastAPI Versioning Strategy

- **Decision**: All content will be developed and tested against the **latest stable version of FastAPI** at the time of writing. Version-specific notes will be added if a feature behaves significantly differently in a recent major version.
- **Rationale**: Focusing on the latest stable version ensures the content is modern and relevant. Attempting to support multiple versions would add significant complexity.
- **Alternatives considered**: Creating separate content branches for each version was deemed too high-maintenance for the project's scope.

## 3. Monorepo Best Practices (FastAPI + React)

- **Decision**: We will use a standard monorepo layout with `backend/` and `frontend/` directories at the root. A tool like `npm` with workspaces (or `pnpm`/`yarn` workspaces) will manage dependencies from the root `package.json`.
- **Rationale**: This is a widely adopted and well-understood pattern for web application monorepos. It provides clear separation of concerns while allowing for shared tooling and configuration.
- **Alternatives considered**: Using more advanced monorepo tools like Nx or Turborepo was considered but adds unnecessary complexity for a two-package project.

## 4. "Real-world" FastAPI Application Structure

- **Decision**: The backend will be structured following a feature-based, layered architecture:
  - **`api/`**: Contains the FastAPI routers and endpoint definitions.
  - **`services/`**: Contains business logic, implemented as classes (e.g., `TutorialService`).
  - **`models/` or `schemas/`**: Contains Pydantic models for data representation and validation.
  - **`core/`**: For application-wide configuration and settings.
  - **`tests/`**: A parallel structure for unit and integration tests.
- **Rationale**: This structure promotes separation of concerns, testability, and scalability, reflecting common patterns seen in mature open-source and enterprise projects.
- **Alternatives considered**: A simpler, flat structure was rejected as it does not scale well and does not align with the project's goal of teaching "real-world" patterns.
