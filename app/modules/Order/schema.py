from pydantic import BaseModel


class Menu_Items(BaseModel):
    menu_id:int
    quantity:int

class Order_Post(BaseModel):
    restaurant_id:int
    user_id:int
    menu_items : list[Menu_Items]