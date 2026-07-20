from app.modules.User.user_schema import User as UserSchema
from app.modules.User.user_model import User
from fastapi import HTTPException

class User_Services:
    async def get_all_user(self):
        return await User.all()
    
    async def create_new_user(self,user:UserSchema):
        if(User.get(id=user.id)):
            raise HTTPException(status_code=404 , detail="User already exist")
        return await User.create(**user.dict())
    
    async def delete_a_user(self,id:int):
        user = await User.get(id=id)
        if(not user.isActive):
            return {"message":"user is already inactive"}
        user.isActive=False
        await user.save()
        return {"message":"user is now inactive"}   
    
    async def update_old_user(self,updatedUser):
        return await User.filter(id=updatedUser.id).update(**updatedUser.dict())
        
