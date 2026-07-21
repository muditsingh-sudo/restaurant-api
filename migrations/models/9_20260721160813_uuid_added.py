from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" ALTER COLUMN "created_at" SET DEFAULT '2026-07-21 16:08:13.755987';
        ALTER TABLE "users" ALTER COLUMN "updated_at" SET DEFAULT '2026-07-21 16:08:13.756006';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" ALTER COLUMN "created_at" SET DEFAULT '2026-07-21 15:20:22.667962';
        ALTER TABLE "users" ALTER COLUMN "updated_at" SET DEFAULT '2026-07-21 15:20:22.667977';"""


MODELS_STATE = (
    "eJztmGtv2jAUhv9KlE+t1KIQrq2mSdyqMgGpIGxTpykyiQGriZ0lTlvW9b/PNrlzEUxL11"
    "X9AuQ958QnT47xsZ9kh1jQ9ktTH3rypfQkY+BA9iOjn0kycN1E5QIFM1s4BsxDKGDmUw+Y"
    "lIlzYPuQSRb0TQ+5FBHMVBzYNheJyRwRXiRSgNGPABqULCBdikS+fWcywhZ8hH506d4Zcw"
    "RtK5MnsvjYQjfoyhXadNrvXglPPtzMMIkdODjxdld0SXDsHgTIKvEYbltADD1AoZV6DJ5l"
    "+LiRtM6YCdQLYJyqlQgWnIPA5jDkD/MAm5yBJEbiH9WPYWopN8MYabox6emGIR/BziSYc0"
    "eYclBPz+v7JkCEKvMBOtet8UmlfioQEJ8uPGEUuORnEQgoWIcK6All6ABkb4LuLIG3HXQc"
    "kGPNUi2GcgSoAKSyAx4NG+IFXbJLtVbbw/hzaywwMy/BmbAZsZ4no9Ckrm2cd8LXBb7/QL"
    "wttbwbcTrm71COhARzMpFjpmW1Uq3VG82Loio4h1s9CLe6B7e6gVt8H4E68n85zP93OZuI"
    "ro7hG/m/8z2Mr08ZjmMAxwHvhA8j/BO5DJ91FOR0zBvkXFYOwFxWdlLmpizkGbABNrcwvr"
    "IJoNshp2JyjOc8qCjKSkl5+Yatq03bg550M+51+pO+NuKjOCv/h50YucQERAWCca81yDFG"
    "fov1nvdbILcJsSHAOxrlVFiO84zFFYU5autelnNb0waCrR+ybff1XBVPh+0eq+7TLO/+SM"
    "+vfB7kSIx1JWaBd5mFIgfuWAMzkTnmVhhain4U1t6pilo/Vxrnalkq1y+V5mW5UmrUahfN"
    "RmH9HntwS8P2Knz/e16U3h/2JnpreJN5W92W3uMWNTs/QvWknvtHim8ifenr1xK/lG61US"
    "+/LYr99FuZ5wQCSgxMHgxgpXYgkRrRzFRD4Fp/WA3ZyFdWDXVFqb9XQ6YaInapchDZ83OL"
    "+V1qT82FGTDvHoBnGRsWopJdvpsmR3XyCsBgId4lh8vTDI9xWtBD5lLecsATWs72HfGAxO"
    "fVnPH08Y4GYesRD6uu/BwJ5+/rPXVY8BTYzKs2qs1KvdpkLiLNWGnsmRvRyrT7SOceej5P"
    "6YgGNxXyBvvbQvYRfFIdQTh0f4N0y8ph24d9+4eNDQQbkUK8ZXH9NNFGO9qsJCS/qiKTSr"
    "8kG/mF7SIKpL0HLoeRWSIjpifD1tc87s5Aa+fXPn6DNkP/Txez5988es1n"
)
