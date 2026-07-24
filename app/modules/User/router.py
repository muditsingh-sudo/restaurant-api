from typing import Annotated

from fastapi import APIRouter, Depends

from app.modules.User.schema import UserCreate, UserOut, UserUpdate
from app.modules.User.services import User_Services

userRouter = APIRouter(prefix="/user" , tags=["user"])

@userRouter.get("/" , response_model=list[UserOut])
async def read_users(user_dependency:Annotated[User_Services , Depends(User_Services)]):
    return await user_dependency.get_all_user()

@userRouter.get("/{id}" , response_model=UserOut)
async def read_user_by_id(id:int,user_dependency:Annotated[User_Services , Depends(User_Services)]):
    return await user_dependency.get_user_by_id(id)

@userRouter.post("/", response_model=UserOut)
async def create_user(user:UserCreate,user_dependency:Annotated[User_Services , Depends(User_Services)]):
    return await user_dependency.create_new_user(user)

@userRouter.delete("/{id}")
async def delete_user(id:int,user_dependency:Annotated[User_Services , Depends(User_Services)]):
    return await user_dependency.delete_a_user(id)

@userRouter.patch("/{id}")
async def update_user(id: int,user_data:UserUpdate,user_dependency:Annotated[User_Services , Depends(User_Services)]):
    return await user_dependency.update_old_user(id , user_data)
