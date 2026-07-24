from tortoise import fields
from tortoise.models import Model


class Owner(Model):
    id=fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.User',related_name='user_owners')
    restaurant = fields.ForeignKeyField('models.Restaurant',related_name='restaurant_owners')

    class Meta:
        table = "owners"


class Restaurant(Model):
    id=fields.IntField(pk=True)
    name= fields.CharField(max_length= 255)
    city = fields.CharField(max_length= 255)
    state = fields.CharField(max_length= 255)
    zip_code = fields.CharField(max_length= 10)

    class Meta:
        table= "restaurants"

class Menu(Model):
    id=fields.IntField(pk=True)
    restaurant = fields.ForeignKeyField('models.Restaurant' , related_name='menu_items')
    name = fields.CharField(max_length= 255)
    info = fields.TextField()
    price = fields.IntField()
    availability = fields.IntField()

    class Meta:
        table = "menu_items"
        