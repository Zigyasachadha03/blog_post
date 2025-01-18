from fastapi import FastAPI
from app.routers import post_router, user_api_router, auth_api_router

app = FastAPI()

app.include_router(post_router)
app.include_router(user_api_router)
app.include_router(auth_api_router)