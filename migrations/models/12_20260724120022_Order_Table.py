from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "orders" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "order_date_time" TIMESTAMPTZ NOT NULL,
    "total_amount" DOUBLE PRECISION NOT NULL,
    "restaurant_id" INT NOT NULL REFERENCES "restaurants" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
        CREATE TABLE IF NOT EXISTS "order_items" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "quantity" INT NOT NULL,
    "amount" DOUBLE PRECISION NOT NULL,
    "menu_item_id" INT NOT NULL REFERENCES "menu_items" ("id") ON DELETE CASCADE,
    "order_id" INT NOT NULL REFERENCES "orders" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "order_items";
        DROP TABLE IF EXISTS "orders";"""


MODELS_STATE = (
    "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"
)
