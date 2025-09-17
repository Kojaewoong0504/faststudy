from fastapi import FastAPI
from src.api import categories, tutorials

app = FastAPI()

# Include routers from the api module
app.include_router(categories.router)
app.include_router(tutorials.router)

@app.get("/")
def read_root():
    return {"message": "Backend server is running"}
