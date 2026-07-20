from fastapi import FastAPI
from app.routes.routes import router
from app.config.connectDB import create_database_connection
from dotenv import load_dotenv
import os

load_dotenv()



app = FastAPI()
create_database_connection(app)

@app.get("/")
def get_root():
    return {os.getenv('DB_USERNAME'):os.getenv('DB_PASSWORD')}

app.include_router(router)

