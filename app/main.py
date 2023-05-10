"""
    Запуск проекта (main-файл).
"""

from fastapi import FastAPI, Request, Response

from .cron import run_cron

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await run_cron()


@app.get("/")
async def index(request: Request, response: Response):
    return {"status": "200"}


@app.get("/ping")
async def test_connection(request: Request, response: Response):
    return {"status": "200"}
