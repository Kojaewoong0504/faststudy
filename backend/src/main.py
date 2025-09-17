from fastapi import FastAPI, HTTPException, status, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from backend.src.core.database import mongodb
from backend.src.api import categories, tutorials
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()

# CORS 설정
origins = [
    "http://localhost",
    "http://localhost:3000", # 프론트엔드 주소
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_db_client():
    logging.info("Connecting to MongoDB...")
    await mongodb.connect()
    logging.info("Connected to MongoDB.")

@app.on_event("shutdown")
async def shutdown_db_client():
    logging.info("Closing MongoDB connection...")
    await mongodb.close()
    logging.info("Closed MongoDB connection.")

# API 라우터 포함
app.include_router(categories.router)
app.include_router(tutorials.router)

# 루트 엔드포인트
@app.get("/")
async def read_root():
    return {"message": "Welcome to FastStudy API"}

# 전역 예외 처리기 (선택 사항: 일관된 에러 응답을 위해)
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logging.error(f"HTTPException: {exc.status_code} - {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.detail,
            "code": exc.status_code
        }
    )

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    logging.exception("An unexpected error occurred.")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "message": "An unexpected error occurred.",
            "code": status.HTTP_500_INTERNAL_SERVER_ERROR
        }
    )
