from fastapi import FastAPI
from controllers.user_controller import router as user_router

app = FastAPI()

app.include_router(user_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the User Management API"}