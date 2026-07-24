from tortoise import fields
from tortoise.models import Model


class Order(Model):
    id=fields.IntField(pk=True)
    restaurant = fields.ForeignKeyField('models.Restaurant' , related_name='orders')
    user = fields.ForeignKeyField('models.User',related_name='orders')
    order_date_time = fields.DatetimeField()
    total_amount = fields.FloatField()

    class Meta:
        table = "orders"

class Order_Items(Model):
    id=fields.IntField(pk=True)
    order = fields.ForeignKeyField('models.Order' , related_name="order_data")
    menu_item = fields.ForeignKeyField('models.Menu',related_name='menu_items')
    quantity = fields.IntField()
    amount = fields.FloatField()

    class Meta:
        table = "order_items"

