from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "restaurants" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL,
    "city" VARCHAR(255) NOT NULL,
    "state" VARCHAR(255) NOT NULL,
    "zip_code" VARCHAR(10) NOT NULL
);
        CREATE TABLE IF NOT EXISTS "menu_items" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL,
    "info" TEXT NOT NULL,
    "price" INT NOT NULL,
    "availability" INT NOT NULL,
    "restaurant_id" INT NOT NULL REFERENCES "restaurants" ("id") ON DELETE CASCADE
);
        CREATE TABLE IF NOT EXISTS "owners" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "restaurant_id" INT NOT NULL REFERENCES "restaurants" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "menu_items";
        DROP TABLE IF EXISTS "owners";
        DROP TABLE IF EXISTS "restaurants";"""


MODELS_STATE = (
    "eJztmm1v2zYQgP+KoE8pkAWx6rxs32THWb3G9pCoW9FhEGiJtolIpCtRcbzO/30kJVrUa+"
    "0uDiJDQIHGxzu+PKR4xyO/6T5xoReefQphoP+ifdMx8CH7IyM/1XSwXKZSLqBg6gnFiGkI"
    "CZiGNAAOZcIZ8ELIRC4MnQAtKSKYq1oLFGrsH9BGvB5ttUDOQnPhDGEYanQBtdBZQB9oZC"
    "Z+iaq1uCVeG3FYCwjPX6CuCKOvEbQpmUNWyof+199MjLALn2Eofy4f7RmCnpshg1xegZDb"
    "dL0UsiGmt0KRd3NqO8SLfJwqL9d0QfBWG2HKpXOIYQAo5NXTIOLAcOR5CVjJMO5pqhJ3Ub"
    "FhYwaRx7Fz67gDqUy37fHEsh8Glm3rhSmRFgrZROQQzKeTdTUUo5/zLvxkdLpX3ev3l91r"
    "piK6uZVcbeKmUzCxocAztvSNKAcUxBqCcQqVzRTyilz7CxCUg90a5NiyTufZSpJvF64Pnm"
    "0P4jldcKIXFzUo/zDv+x/M+xOm9Y43SdgnF3+I46TIiMs475TvEoThigQlS7casWrzMpSl"
    "IMWc7hRbph3jfffi8ur6Z/11cBs74TZqcBsF3OL/PVBL/dfD3Ozl7CC63oev1G/57sY3pA"
    "zHPoC3Bi3h3Qj/g5YMn7sXZNXmCDl3znfA3DmvpMyLspCnwAPYKWF8Ax3kA68cs2KVo+zG"
    "ZmeJeQOJ1xC+GfSHI/PupGOcGoJx+NVDFKrwuwXCKDQdip5KEPcI8SDAFWGxYpZjPGV2hw"
    "Irg7rXBdubTO54zX7IiArB0Mqt4U+j3oCt7Rx2GTYrfi+AHIkNaMmaZiUU+bDCA2Ys8+s6"
    "MT2TfzRwZetsgO4Ee+tknmsmxBqOBg+WOfo9Mys3pjXgJYaQrnPSk8vcvrOtRPtzaH3Q+E"
    "/ty2Q8EHhJSOeBaDHVs77ovE8gosTGZGUDVzlnSKmklpn1aOn+4KxnLdtZfyuzLhkp0y56"
    "z5MOs0flhMwFU+A8rkDg2pkSZXmEMLDJCid5mNw2nBjffryHHhB4iyshSfZMeB0NXAQbue"
    "ylVMVJDFLFs1jkG35eAjCYiyHxtnlLCawRxJFekjET8tO6jJnPNGy2xfu7pc2qMbRJrLeV"
    "xGpP/Yc9MyE8I0W+FnyuWreJ/lHwrfNsg89WxqlJiicj8/O7jGO7m4x/leoK9f7dpJfPGA"
    "ao7ORUuUls9b+/TzSA9stsFSlN8AQQGyvyShNXlVDzZi3bErYs5KIgCgCm9l5urWDX0k3o"
    "FsLQMthF0rckgGiOP8K1AD5k/apIpCSx0n2msoaBroo6mTgAq23MVVxmjAMbPYzP+H3zoW"
    "/eDPRNdaR/yCg2DvlLwtjtWaA6jk2PHG0M26jPuy6GbTfTQ7oqcVTfi6ti0RL9vnuKkvcq"
    "/9MxyWcvDYO7q0tSFlW5MyoPr1qPfwQeX5mBErefnZ9q358OsQ0AjisAaJNY7dOVJvNtn6"
    "60T1ca+nTlh27/lGCjfOve5wZQXl41bDIqLwAr0oTtZekrX5aaMEDOoizgTEpqg02Q6rRx"
    "5rHEmU/sC0w+sF2diGJyhD7kIL6af1R7EE7Uj5Bu53w3F13nowuvH1mLFJblRX57mIwrwv"
    "nUJP8cCzlU+1fzUNjg3EgZXA6j/no6fxN9mn1MxSvo7Rcfvbwz2/wHF72lww=="
)
