from fastapi import APIRouter
from app.modules.User.router import userRouter
from app.modules.Restaurant.router import restaurantRouter

router = APIRouter()

router.include_router(userRouter)
router.include_router(restaurantRouter)