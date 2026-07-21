from fastapi import APIRouter

restaurantRouter = APIRouter(prefix="/restaurant",tags=["restaurant"])

@restaurantRouter.get("/")
async def get_gertaurant():
    return {"Name":"Misthan bhandar"}