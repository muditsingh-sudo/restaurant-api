from decimal import Decimal

from fastapi import HTTPException
from tortoise import timezone

from app.modules.Order.model import Order, Order_Items
from app.modules.Order.schema import Order_Post
from app.modules.Restaurant.model import Menu, Restaurant
from app.modules.User.model import User


class Order_Services:

    async def create_order(self,order_data : Order_Post):
        restaurant_id = order_data.restaurant_id
        user_id = order_data.user_id

        restaurant_exist = await Restaurant.get_or_none(id=restaurant_id)
        user_exist = await User.get_or_none(id=user_id)

        if(not restaurant_exist or not user_exist or not user_exist.isActive):
            raise HTTPException(status_code=404 , detail="User or Restaurant not found")

        # validation

        menu_items = order_data.menu_items

        amount = 0.0

        for menu_item in menu_items:
            menu_exist = await Menu.get_or_none(id=menu_item.menu_id)
            print(f"ID: {menu_exist.id}, Name: {menu_exist.name}, Price: {menu_exist.price}, Stock: {menu_exist.availability}")
            if not menu_exist or menu_exist.availability < menu_item.quantity:
                print(menu_exist.availability , menu_item.quantity)
                raise HTTPException(status_code=404 , detail="Items quantity unvaliable")

            amount += menu_item.quantity * menu_exist.price

        if user_exist.balance < amount:
            raise HTTPException(status_code=404 , detail="Amount too low")

        try:
            print(restaurant_exist.id , user_exist.id , amount)
            order_created = await Order.create(
                restaurant=restaurant_exist,
                user=user_exist,
                order_date_time=timezone.now(),
                total_amount = amount
            )
            print("hello")

            user_exist.balance = user_exist.balance - Decimal(str(amount))

            order_items_create = list()

            for menu_item in menu_items:
                menu_exist = await Menu.get_or_none(id=menu_item.menu_id)
                order_item = await  Order_Items.create(
                    order = order_created ,
                    menu_item = menu_exist,
                    quantity = menu_item.quantity,
                    amount=menu_item.quantity * menu_exist.price 
                )
                menu_exist.availability = menu_exist.availability - menu_item.quantity
                await menu_exist.save()
                order_items_create.append(order_item)

            await user_exist.save()
            return {
                "order":order_created,
                "items": order_items_create
            }
        except Exception as e:
            raise HTTPException(status_code=500 , detail=str(e))
