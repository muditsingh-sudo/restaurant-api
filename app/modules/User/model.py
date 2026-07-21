from tortoise import Model,fields

class User(Model):
    """This is a Model which defines the schema of the users table"""
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length= 255 , unique=True)
    password = fields.CharField(default ="123456789",max_length=225)
    name = fields.CharField(max_length= 255)
    city = fields.CharField(max_length= 255)
    state = fields.CharField(max_length= 255)
    zip_code = fields.CharField(max_length= 10)
    balance = fields.DecimalField(max_digits=12, decimal_places=2) 
    isActive = fields.BooleanField(default=True)
    created_at = fields.DatetimeField( auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table= "users"
