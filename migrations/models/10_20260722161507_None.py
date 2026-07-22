from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "password" VARCHAR(225) NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "city" VARCHAR(255) NOT NULL,
    "state" VARCHAR(255) NOT NULL,
    "zip_code" VARCHAR(10) NOT NULL,
    "balance" DECIMAL(12,2) NOT NULL,
    "isActive" BOOL NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL,
    "updated_at" TIMESTAMPTZ NOT NULL
);
COMMENT ON TABLE "users" IS 'This is a Model which defines the schema of the users table';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztmG1v2jAQx79KlFdM6qqS0pbtXaBMZSowtek2dZoikxhi1bHT2CllXb/7bCchjzCY2q"
    "5USEgk/7uzL79z4ocH3acuxGz/isFQ/6g96AT4UFwU9D1NB0GQqVLgYIyVYyQ8lALGjIfA"
    "4UKcAMygkFzInBAFHFEiXS0PMU38gDaQ7WgzDzme5sIJIpBp3IMaczzoA41O1J1qWot7kq"
    "1RR/SAyPQJ2ooIuo2gzekUCqt89B8/hYyIC+8hS2+DG3uCIHYLZJArG1C6zeeB0vqEf1KO"
    "Ms2x7VAc+SRzDubco2ThjQiX6hQSGAIOZfM8jCQwEmGcgE0ZxplmLnGKuRjxzCDCEruMjh"
    "PINN22hyPLvuxZtq1XSpJG5MgmkkOJLKdIlamnn8oU3hvN1kmrfXjcagsXleZCOXmMu87A"
    "xIEKz9DSH5UdcBB7KMYZVFEphKtcux4I68EuAkpsRdJltinJ1wvXB/c2hmTKPUn06GgFyq"
    "/mRffMvGgIr3eySypeufhFHCYmI7ZJ3hnfADA2o2HN0F2OOB/zNJRTIcOcfSkWTJvGYevo"
    "+KT9QX8Z3MZauI0VuI0KbvW/AerU/+Uwb/dwdhCfb8I39d/xXY8v4wLHJoAXATvC6xH+hQ"
    "KBz90Icj7mDXJuHqyBuXmwlLI0FSGPAQbEqWF8Ch3kA1yPORdVouzGYftJ+BYSX0H4tNft"
    "D8zzRtPYMxRjdosRh3n4rQphxEyHo7saxB1KMQRkybI4F1ZiPBZxzwU2XdS9LNjOaHQuW/"
    "aZIKqEvlUaw1eDTk+M7RL2dNmcm/dCKJHYgNeMaWHhyIdLZsBCZHlcJ6H76cUWjmxdPKA7"
    "Inie1HlFQaz+oHdpmYMvhaqcmlZPWgylzktq47j03Vk0on3rW2eavNWuR8OewksZn4aqx8"
    "zPutZlTiDi1CZ0ZgM3t89I1ZRaoepR4P5j1YuRu6q/lqqnjHJlV9nLQ4fJTW6HLIUxcG5m"
    "IHTtioUadJlv1eQbflkBBExVzSRcmWZy6mPCEDmeXnMelFj2Vp0Igcznb0dCy+u8O6B5XQ"
    "c0dzBkMqUNlqu5kDe4Wn2WXYF8qTYgnLi/QbrNg/U2A6t2A5XFquiRQ1IziX6+HA2XLJuy"
    "kPLsiRyu/dYwYpVvxRbQXgFXwihMkSnTxsD8XsbdPR91ynOfbKAj0P/XyezxD0je5eY="
)
