# FastAPI Learning Hub

This project aims to provide a practical, real-world focused learning platform for FastAPI development. Unlike typical documentation, it emphasizes patterns and practices commonly found in enterprise environments, such as class-based service layers and monorepo structures.

## Features

-   **Monorepo Structure**: Manages both backend (FastAPI) and frontend (React) within a single repository.
-   **Practical FastAPI Patterns**: Focuses on real-world implementation details beyond basic documentation.
-   **Modular Backend**: Organized with dedicated modules for API, services, and models.
-   **Component-Based Frontend**: Built with React, featuring reusable components for categories and tutorials.
-   **Comprehensive Setup Guide**: Easy-to-follow instructions for setting up the development environment.

## Quickstart Guide

This guide provides the steps to set up and run the development environment for this project.

### Prerequisites

- Node.js (v20+)
- Python (v3.11+)
- `pip` and `venv` for Python package management

### Setup & Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Set up the Backend (FastAPI)**:
    ```bash
    # Navigate to the backend directory
    cd backend

    # Create and activate a virtual environment
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

    # Install Python dependencies
    pip install -r requirements.txt
    ```

3.  **Set up the Frontend (React)**:
    ```bash
    # Navigate to the frontend directory from the root
    cd frontend

    # Install Node.js dependencies
    npm install
    ```

### Running the Development Servers

-   **Run the Backend Server**:
    -   Make sure you are in the `backend/` directory with the virtual environment activated.
    ```bash
    uvicorn src.main:app --reload
    ```
    -   The API will be available at `http://127.0.0.1:8000`.

-   **Run the Frontend Server**:
    -   Make sure you are in the `frontend/` directory.
    ```bash
    npm start
    ```
    -   The React application will be available at `http://localhost:3000`.

## Project Structure

This project uses a monorepo structure:

-   `backend/`: Contains the FastAPI application.
-   `frontend/`: Contains the React application.
-   `package.json` (root): Manages monorepo workspaces and common scripts.

## Testing

-   **Backend Tests**: Navigate to the `backend/` directory and run `pytest`.
-   **Frontend Tests**: Navigate to the `frontend/` directory and run `npm test`.

## Contributing

Contributions are welcome! Please refer to the `CONTRIBUTING.md` (to be created) for guidelines.
