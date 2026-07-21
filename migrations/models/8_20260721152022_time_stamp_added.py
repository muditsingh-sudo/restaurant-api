from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" ADD "updated_at" TIMESTAMPTZ NOT NULL DEFAULT '2026-07-21 15:20:22.667977';
        ALTER TABLE "users" ADD "created_at" TIMESTAMPTZ NOT NULL DEFAULT '2026-07-21 15:20:22.667962';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" DROP COLUMN "updated_at";
        ALTER TABLE "users" DROP COLUMN "created_at";"""


MODELS_STATE = (
    "eJztmFtv2jAUx79KlKdWaquQcmn7FihVmYBUkG5TpykyiQGriZ3FTlvW9bvPNgm5cBFMC+"
    "sqnoD/OSc+/uUYH/tV9YkLPXp2T2GoXimvKgY+5F9y+omigiBIVSEwMPKkY8Q9pAJGlIXA"
    "YVwcA49CLrmQOiEKGCKYqzjyPCEShzsiPEmlCKMfEbQZmUA2lYl8+85lhF34AmnyM3i0xw"
    "h6bi5P5IqxpW6zWSC1DmY30lGMNrId4kU+Tp2DGZsSvPBGmAl1AjEMAYPi8SyMRPoiu3ia"
    "yYzmmaYu8xQzMS4cg8hjmemO7FRTbbtvWvawbdm2ugMgh2ABl6dK5ewnIoVTvVJtVC/O69"
    "UL7iLTXCiNt/nQKZh5oMTTt9Q3aQcMzD0k4xQq9AHylrm2piBcDXYRUGDLky6yTUi+X7g+"
    "eLE9iCdsKojWahtQfjYGrVtjcMS9jsWQhC+A+bLoxyZ9bhO8U74BoPSZhCtKdz3ibMzfoZ"
    "wIKeZ03S6YVvTzaq3euLhU94Nb3wq3vgG3voRbfu6AOvHfH+b/u5wdxGa78E38D3y340sZ"
    "x7EL4EXAgfB2hH+igONzd4KcjfmAnCvaFpgr2lrKwpSHPAIewM4KxjceAWs6tkxMgfFYBJ"
    "VFWTvTSoK8Aeq1ed/stpW7QbvVGXbMvhjFn9EfXmoUEhcQkwgGbaNbYIyo4TD0tAJykxAP"
    "ArymMc6EFTiPeFxZmJO2br+cm6bZlWxpzLbZsQpVfN9rtnl1H+d5J41zZucLoUBizysxD/"
    "yaWxjy4Zo9MBdZYO7GoWfJl9LaO13T66dagx8llErtSteudP2sXm9c1vXS+j0+cdfE3ix+"
    "/xtelNXptYeW0bvLva1rw2oLi55fH7F6VC/8Iy0eonzpWLeK+Kk8mH25lAJC2SSUI6Z+1o"
    "MqcgIRIzYmzzZwMyeQRE1o5qohCtw/rIZ85LurhkbjUA25akjYZcpBZi+uKcaPmTO1EEbA"
    "eXwGoWsvWYhO1vkum3zdLyoAg4l8lwKuSDO+tTFgiJypuuI+J7acbLrRAanP4Upnb81XyV"
    "c6TzCkIqUdGtxMyAfsb0s5R4hFtQPh2P0D0q1o2x0fNp0flg4QfEQG8YrN9dPQ7K9ps9KQ"
    "4q6KHKb8UjxESztFlEh7A1wBI7dFJkyPesbXIu5W12wW9z7xgCZH/083s7ffB8PFiw=="
)
