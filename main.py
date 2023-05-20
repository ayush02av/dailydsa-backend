from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import router
from config import config

app = FastAPI(title=config.PROJECT_TITLE, version=config.PROJECT_VERSION)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)