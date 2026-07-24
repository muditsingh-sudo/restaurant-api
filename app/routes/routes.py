from fastapi import APIRouter

from app.modules.Auth.router import authRouter
from app.modules.Order.router import orderRouter
from app.modules.Restaurant.router import restaurantRouter
from app.modules.User.router import userRouter

router = APIRouter()

router.include_router(authRouter)

router.include_router(userRouter)

router.include_router(restaurantRouter)

router.include_router(orderRouter)
