from app.modules.User.model import User
from app.modules.User.schema import UserCreate , UserUpdate

from fastapi import HTTPException

class User_Services:
    """This is the class which does all the endpoint operation and interact with the DB"""

    async def get_all_user(self):
        """This function returns all the users in the DB"""
        try:
            return User.all()
        except Exception:
            raise HTTPException(status_code=500 , detail="Error fetching data")
    
    async def get_user_by_id(self, id:int):
        try:
            user = await User.get(id=id)
            return user
        except Exception:
            raise HTTPException(status_code=500 , detail="User not found")
    
    async def create_new_user(self,user:UserCreate):
        """This fuction creates a new user in the DB"""
        duplicate = await User.get_or_none(email=user.email)

        if(duplicate):
            raise HTTPException(status_code=400 , detail="User already exist")
            
        try:
            return await User.create(**user.dict())
        except Exception as e:
            raise HTTPException(status_code=400,detail= "given data is worong")
    
    async def delete_a_user(self,id:int):
        """This function is used to soft delete a user"""
        try:
            user = await User.get_or_none(id=id)

            if(not user):
                raise HTTPException(status_code=404 , detail="user id donot exist")

            if(not user.isActive):
                return {"message":"user is already inactive"}
        
            user.isActive=False
            await user.save()
            return {"message":"user is now inactive"}   
        except Exception as e:
            raise HTTPException(status_code=404 , detail = str(e))
    
    async def update_old_user(self, id: int, user_data : UserUpdate):      
        """This function is used to update and existing user"""

        user = await User.get_or_none(id=id)

        if not user:
            raise HTTPException(status_code=400, detail="User not found")
        
        try:
            update_payload = user_data.model_dump(exclude_unset=True)
            user.update_from_dict(update_payload)
            await user.save()
            return user
        except Exception as e:
            raise HTTPException(status_code=400 , detail=str(e))
        