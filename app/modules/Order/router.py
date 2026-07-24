from typing import Annotated

from fastapi import APIRouter, Depends

from app.modules.Order.schema import Order_Post
from app.modules.Order.services import Order_Services

orderRouter = APIRouter(prefix="/order",tags=["order"])

@orderRouter.post("/" )
async def create_order(order_data : Order_Post , order_services :Annotated[Order_Services,Depends(Order_Services)] ):
    return await order_services.create_order(order_data)