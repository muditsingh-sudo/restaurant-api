from tortoise.contrib.fastapi import register_tortoise
from app.config.TORTOISE_ORM import TORTOISE_ORM

def create_database_connection(app):
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=False,
        add_exception_handlers=True
    )
