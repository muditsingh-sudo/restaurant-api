from fastapi import HTTPException

from app.modules.Restaurant.model import Menu, Owner, Restaurant
from app.modules.Restaurant.schema import (
    add_menu_schema,
    assing_owner_schema,
    create_restaurant_schema,
    menu_update,
)
from app.modules.User.model import User


class Restaurant_Service:

    async def get_all_restaurant(self):
        try:
            return await Restaurant.all()
        except Exception as e:
            raise HTTPException(status_code=500 , detail=str(e))

    async def create_new_retaurant(self , restaurant_data:create_restaurant_schema):
        ownerId = restaurant_data.owner_id
        restaurant_dict = restaurant_data.model_dump(exclude={'owner_id'})
        
        try:
            user = await User.get(id=ownerId)
            restaurant = await Restaurant.create(**restaurant_dict)
            owner = await Owner.create(user=user , restaurant = restaurant)
            return {
                "message":"Restaurant created ",
                "id":owner.id,
                "user":owner.user_id,
                "retaurant":owner.restaurant_id
            }
        
        except Exception as e: 
            raise HTTPException(status_code=500 , detail=str(e))


    async def add_menu_item(self,restaurant_id:int , menu_data:add_menu_schema ):
        print("hello")
        try:
            print(menu_data)
            menu_item = await Menu.create(restaurant_id=restaurant_id , **menu_data.model_dump())
            return menu_item
        except Exception as e:
            raise HTTPException(status_code=500 , detail=str(e))

    async def update_menu_item(self, menu_id :int , update_menu_data:menu_update):
        menu_exist = await Menu.get_or_none(id=menu_id)

        if not menu_exist :
            raise HTTPException(status_code=404, detail="menu item not found")

        menu_payload = update_menu_data.model_dump(exclude_unset=True)
        menu_exist.update_from_dict(menu_payload)
        await menu_exist.save()
        return menu_exist

    async def get_restaurant_menu(self,restaurant_id:int):
        try:
            menu_items = await Menu.filter(restaurant_id = restaurant_id)
            return menu_items
        except Exception as e:
            raise HTTPException(status_code=500 , detail=str(e))

    async def assing_owner(self, assingment_data:assing_owner_schema):
        user_id = assingment_data.user_id
        restaurant_id = assingment_data.restaurant_id

        user_exist = await User.get_or_none(id=user_id)

        if not user_exist or not user_exist.isActive:
            raise HTTPException(status_code=400 , detail="User does not exists")

        restaurant_exist = await Restaurant.get_or_none(id=restaurant_id)

        if not restaurant_exist :
            raise HTTPException(status_code=400, detail="Restaruant does not exists")

        try:
            owner_assinged = await Owner.create(**assingment_data.model_dump())
            return owner_assinged
        except Exception as e:
            raise HTTPException(status_code=500 , detail=str(e))
