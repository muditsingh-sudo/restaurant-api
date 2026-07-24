from typing import Annotated

from fastapi import APIRouter, Depends

from app.modules.Restaurant.schema import (
    add_menu_schema,
    assing_owner_schema,
    create_restaurant_schema,
    menu_update,
)
from app.modules.Restaurant.services import Restaurant_Service

restaurantRouter = APIRouter(prefix="/restaurant",tags=["restaurant"])

@restaurantRouter.get("/")
async def get_gertaurant(restaurant_service:Annotated[Restaurant_Service,Depends(Restaurant_Service)]):
    return await restaurant_service.get_all_restaurant()

@restaurantRouter.post("/")
async def create_restaurant(restaurant_data:create_restaurant_schema , restaurant_service:Annotated[Restaurant_Service,Depends(Restaurant_Service)]):
    return await restaurant_service.create_new_retaurant(restaurant_data)

@restaurantRouter.post("/assing_owner")
async def assing_owner(assingment_data:assing_owner_schema , restaurant_service:Annotated[Restaurant_Service,Depends(Restaurant_Service)] ):
    return await restaurant_service.assing_owner(assingment_data)

@restaurantRouter.post("/{restaurant_id}/menu")
async def add_menu_item(restaurant_id:int ,menu_data : add_menu_schema ,restaurant_service:Annotated[Restaurant_Service,Depends(Restaurant_Service)]):
    return await restaurant_service.add_menu_item(restaurant_id,menu_data)

@restaurantRouter.get("/{restaurant_id}/menu")
async def get_restaurant_menu(restaurant_id:int ,restaurant_service:Annotated[Restaurant_Service,Depends(Restaurant_Service)] ):
    return await restaurant_service.get_restaurant_menu(restaurant_id)

@restaurantRouter.patch("/{restaurant_id}/{menu_id}" )
async def update_menu_item(restaurant_id:int, menu_id:int,update_menu_data:menu_update , restaurant_service:Annotated[Restaurant_Service,Depends(Restaurant_Service)] ):
    return await restaurant_service.update_menu_item(menu_id ,update_menu_data)