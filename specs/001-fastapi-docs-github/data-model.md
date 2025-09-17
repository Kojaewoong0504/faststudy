# Data Models

This document defines the core data entities for the feature based on the feature specification.

## Entity: Category

Represents a grouping of related learning tutorials.

**Attributes**:
- `id` (string, unique): A unique identifier for the category (e.g., "project-structure").
- `name` (string): The human-readable name of the category (e.g., "Project Structure").
- `description` (string): A brief summary of the category.

## Entity: Tutorial

Represents a single learning module or topic.

**Attributes**:
- `id` (string, unique): A unique identifier for the tutorial (e.g., "class-based-services").
- `category_id` (string): The ID of the category this tutorial belongs to.
- `title` (string): The title of the tutorial (e.g., "Implementing Class-Based Services").
- `content` (string, markdown): The full content of the tutorial, including explanations and code snippets.
- `author` (string, optional): The author of the tutorial content.
