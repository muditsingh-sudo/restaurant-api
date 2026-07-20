from fastapi import APIRouter
from app.modules.User.user_services import User_Services
from app.modules.User.user_schema import User as UserSchema

userRouter = APIRouter(prefix="/user" , tags=["user"])

userObj = User_Services()

@userRouter.get("/")
async def read_users():
    return await userObj.get_all_user()

@userRouter.post("/")
async def create_user(user:UserSchema):
    return await userObj.create_new_user(user)

@userRouter.delete("/{user_id}")
async def delete_user(user_id:str):
    return await userObj.delete_a_user(user_id)

@userRouter.patch("/")
async def update_user(user_data:UserSchema):
    return await userObj.update_old_user(user_data.id,user_data)