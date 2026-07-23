from fastapi import APIRouter
from app.modules.User.router import userRouter
from app.modules.Restaurant.router import restaurantRouter
from app.modules.Auth.router import authRouter

router = APIRouter()

router.include_router(authRouter)
router.include_router(userRouter)

router.include_router(restaurantRouter)