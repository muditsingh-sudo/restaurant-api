from app.config.model_list import models
from app.config.settings import DB_PASSWORD, DB_USERNAME

connection_str = f"postgres://{DB_USERNAME}:{DB_PASSWORD}@localhost:5432/restaurant_api?schema=public"

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
