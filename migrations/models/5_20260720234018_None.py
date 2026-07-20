from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "name" VARCHAR(255) NOT NULL,
    "city" VARCHAR(255) NOT NULL,
    "state" VARCHAR(255) NOT NULL,
    "zip_code" VARCHAR(10) NOT NULL,
    "balance" DOUBLE PRECISION NOT NULL,
    "isActive" BOOL NOT NULL
);
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
    "eJztl11v2jAUhv8KylUrdRUwula7SxjVmCiZ+JgmTVPkJCZYOHYaO11px3+f7SQ4hA8Rae"
    "kmxBXwnvfEx49ifM6rEVIfYnY9ZTA2PjZeDQJCKL5s6FcNA0SRVqXAgYuVMREOpQCX8Rh4"
    "XIgzgBkUkg+ZF6OII0qEShKMpUg9YUQk0FJC0GMCHU4DyOeqkB8/hYyID58hy39GC2eGIP"
    "Y36kS+XFvpDl9GSusTfq+McjXX8ShOQqLN0ZLPKVm7EeFSDSCBMeBQPp7HiSxfVpdtM99R"
    "Wqm2pCUWcnw4Awnmhe26jtYMxxnaE2fcmziOUQGQR4mEK0plaveBLOFdu9W57dy9/9C5Ex"
    "ZV5lq5XaVLazBposIznBgrFQccpA7FWEOFIUB4m2t3DuLdYNcJJbai6DLbnOT/CzcEzw6G"
    "JOBzSfTm5gDKb+ao+9kcXQjXpVySigOQHothFmqnMclb81WfFfDm/r9DNxc0Xn1eT4Ovh/"
    "iyCt/cf+Z7HF/GBY4qgNcJZ8LHEX5BkcDnV4JczDlBzq3mEZhbzb2UZWgTsgswIN4OxveY"
    "gj0tRCGnxHgmk+qi3Lxu1gT5ANRP9tQa9BpfR71uf9y3h3KVcMkesQ5KSQiIKwSjnjkoMU"
    "bM9Dh62gHZohRDQPZ0aoW0EmdX5NWFOe8z3pazZdsDxZZlbK3+pPQWTx+snni7Lzd5p52c"
    "7I1ni0IjJwUXeItfIPadrQht033e7VDYDssKICBQ+OQ+5a6yUcGEMfLmxo4hIotcHRojgP"
    "ac54g3+4OteY54EqOhLKnCJVZIOcE7rJZeQR6qCoQz+wnSbTWPaxEO9QhbTYJYkcP0aG8S"
    "/jK2h3vGCZ1Souwjjzd+NzBitXUKNdI+AFfC2LjCcqYXD+b3Mu7uwLYUHMp4EKunqAdY//"
    "oyW/0BevoKkw=="
)
