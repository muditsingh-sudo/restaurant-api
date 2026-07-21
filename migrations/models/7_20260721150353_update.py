from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" RENAME TO "users";
        ALTER TABLE "users" ALTER COLUMN "password" TYPE VARCHAR(225) USING "password"::VARCHAR(225);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" RENAME TO "user";
        ALTER TABLE "users" ALTER COLUMN "password" TYPE VARCHAR(20) USING "password"::VARCHAR(20);"""


MODELS_STATE = (
    "eJztl11v2jAUhv8KylUrdRWkUNjuCKMaEyUTpdOkaYqcxAQLx05jpy3r+t9nOwSH8CEiLW"
    "yruALe8574+FGMz3kxQupDzC7vGYyND7UXg4AQii9r+kXNAFGkVSlw4GJlTIRDKcBlPAYe"
    "F+IUYAaF5EPmxSjiiBKhkgRjKVJPGBEJtJQQ9JBAh9MA8pkq5PsPISPiw2fIsp/R3JkiiP"
    "21OpEv11a6wxeR0gaE3yijXM11PIqTkGhztOAzSlZuRLhUA0hgDDiUj+dxIsuX1S23me0o"
    "rVRb0hJzOT6cggTz3HZdR2uG44zsiXPXnziOUQKQR4mEK0plaveBLOGd2Wi2m52r62ZHWF"
    "SZK6X9mi6twaSJCs9oYryqOOAgdSjGGioMAcKbXHszEG8Hu0oosBVFF9lmJP9duCF4djAk"
    "AZ9Joq3WHpRfu+Pep+74TLjO5ZJUHID0WIyWITONSd6abwQYe6Lxlld3N+J8zp+hnAkasz"
    "63K6YN86rZum533hvHwW0ehNvcg9vcwK0+S6DO/MfD/H+/zh7iizJ8M/+J72F8GRc4ygBe"
    "JZwIH0b4J4oEPr8U5HzOG+TcqB+AuVHfSVmG1iG7AAPibWF8gynY0bHlcgqMpzKpKsr1y3"
    "pFkPdA/WjfW8N+7cu43xvcDeyRXCVcsAesg1ISAuIKwbjfHRYYI9b1OHrcAtmiFENAdjTG"
    "ubQCZ1fkVYU5a+uOy9my7aFiy5ZsrcGk8Bbf31p98Xafr/NOG2c5ikznub5ZCi7w5k8g9p"
    "2NCDXpLu9mKDTDogIICBQ+uU+5q+Vk1oUx8mbGlpltGbnYN7UB7TmNbUf7g614bHsUk7gs"
    "qcQllkt5g3dYJb2CPFQlCC/tb5Buo35Yi7CvR9hoEsSKHKZHe53w5zt7tGOc0CkFyj7yeO"
    "1XDSNWWadQIe09cCWMtSssY3p22/1WxN0b2paCQxkPYvUU9QDrb19mr78B1Vp9hA=="
)
