from fastapi import APIRouter
from app.modules.User.user_router import userRouter
from app.modules.Restaurant.restaurant_router import restaurantRouter

router = APIRouter()

router.include_router(userRouter)
router.include_router(restaurantRouter)