# Quickstart Guide

This guide provides the steps to set up and run the development environment for this project.

## Prerequisites

- Node.js (v20+)
- Python (v3.11+)
- `pip` and `venv` for Python package management

## Setup & Installation

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

## Running the Development Servers

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
