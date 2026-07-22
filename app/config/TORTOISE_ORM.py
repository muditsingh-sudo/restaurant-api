import os
from dotenv import load_dotenv
load_dotenv()
from app.config.model_list import models

connection_str = f"postgres://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@localhost:5432/restaurant_api?schema=public"

TORTOISE_ORM = {
    "connections": {
        # Explicitly declare the schema inside the connection string
        "default": connection_str
    },
    "apps": {
        "models": {
            "models": models,  # Point to your models file
            "default_connection": "default"
        }
    },
}
