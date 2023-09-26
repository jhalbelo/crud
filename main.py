from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="Rest API to MongoDB",
    description="Test whit API",
    version="0.0.2"
)

app.include_router(user)
