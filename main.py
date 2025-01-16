from fastapi import FastAPI
from app.routers import post_router

app = FastAPI()

app.include_router(post_router)