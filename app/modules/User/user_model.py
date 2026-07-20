from tortoise import Model,fields

class User(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length= 255 , unique=True)
    name = fields.CharField(max_length= 255)
    city = fields.CharField(max_length= 255)
    state = fields.CharField(max_length= 255)
    zip_code = fields.CharField(max_length= 10)
    balance = fields.FloatField(default=0.0)
    isActive = fields.BooleanField(default=True)

    class Meta:
        table = "users"