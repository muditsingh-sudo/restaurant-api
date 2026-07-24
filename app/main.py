import os

from dotenv import load_dotenv
from fastapi import FastAPI

from app.config.connectDB import create_database_connection
from app.routes.routes import router

load_dotenv()

app = FastAPI()

# Only connect to the database if NOT running tests
if "pytest" not in os.environ.get("PYTEST_CURRENT_TEST", ""):
    create_database_connection(app)

@app.get("/")
def get_root():
    return {"message": "Server is running"}

app.include_router(router)
