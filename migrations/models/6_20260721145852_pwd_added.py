from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" RENAME TO "user";
        ALTER TABLE "user" ADD "password" VARCHAR(20) NOT NULL DEFAULT '123456789';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" RENAME TO "users";
        ALTER TABLE "user" DROP COLUMN "password";"""


MODELS_STATE = (
    "eJztl11v2jAUhv8KylUrdRVQKGx3hFGNiZKJ0mnSNEVOYoKFY6ex05Z1/e+zHYJDIIhIC9"
    "sqrkrf8574+JE/jl+MgHoQs8t7BiPjQ+3FICCA4seGflEzQBhqVQocOFgZ49ThMB4Blwtt"
    "BjCDQvIgcyMUckSJUEmMsRSpK4yI+FqKCXqIoc2pD/lc1fH9h5AR8eAzZOm/4cKeIYi9jT"
    "KRJ8dWus2XodKGhN8ooxzNsV2K44Boc7jkc0rWbkS4VH1IYAQ4lJ/nUSzLl9WtZpnOKKlU"
    "W5ISMzkenIEY88x0HVtrhm2Pral9N5jatlECkEuJhCtKZWr2vizhXbPR6rS6V9etrrCoMt"
    "dK5zUZWoNJEhWe8dR4VXHAQeJQjDVUGACEt7n25yDaDXadkGMris6zTUn+u3AD8GxjSHw+"
    "l0Tb7T0ov/Ym/U+9yZlwncshqdgAya4Yr0LNJCZ5a74hYOyJRjuWbjHibM6foZwKGrPet2"
    "umjeZVq33d6b43joO7fgjtejHsep61+luCc+o/HuP/ey27iC/L8E39J76H8WVc4CgDeJ1w"
    "InwY4Z8oFPi8UpCzOW+Qc+OQY7hRfAw3to5hB2BA3B2MbzAFBe1aJifHeCaTqqJcv6xXBH"
    "kP1I/WvTka1L5MBv3h3dAay1GCJXvAOiglISCuEEwGvVGOMWI9l6PHHZBNSjEEpKArzqTl"
    "ODsiryrMaU93XM6mZY0UW7Ziaw6nuVV8f2sOxOo+3+SddM3yHTJbZJpmKTjAXTyByLO3Ir"
    "RJi7zboaAZ5BVAgK/wyXnKWa1eZT0YIXdu7HivrSIX+15sQHtOb7ajHbAVv9keYcRkSSUu"
    "sUzKG7zDKukV5KYqQXhlf4N0G/XDWoR9PcJWkyBG5DDZ2puEP99Z44LnhE7JUfaQy2u/ah"
    "ixyjqFCmnvgSthbFxhKdOz2963PO7+yDIVHMq4H6mvqA+Yf/sye/0NA3B8bA=="
)
