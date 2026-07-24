from fastapi import HTTPException

from app.core.security import hash_password
from app.modules.User.model import User
from app.modules.User.repository import UserRepository
from app.modules.User.schema import UserCreate, UserUpdate


class User_Services:
    """This class contains all the user operations and business logic"""

    repository = UserRepository()
        
    async def get_all_user(self):
        """This function returns all the users in the DB"""
        try:
            return await self.repository.get_all()
        except Exception:
            raise HTTPException(status_code=500 , detail="Error fetching data")
    
    async def get_user_by_id(self, id:int):
        """This function returns a specific user by their ID"""
        try:
            user = await self.repository.get_by_id(id)
            return user
        except Exception:
            raise HTTPException(status_code=500 , detail="User not found")
    
    async def create_new_user(self,user:UserCreate):
        """This function creates a new user in the DB"""
        duplicate = await self.repository.get_by_email(user.email)

        if(duplicate):
            raise HTTPException(status_code=400 , detail="User already exist")

        user.password = hash_password(user.password)
            
        try:
            return await self.repository.create(user)
        except Exception as e:
            raise HTTPException(status_code=400,detail= "given data is worong")
    
    async def delete_a_user(self,id:int):
        """This function soft deletes a user by setting them inactive"""

        user = await self.repository.get_by_id(id)

        if(not user or not user.isActive):
            raise HTTPException(status_code=404 , detail="user id donot exist")
        
        user.isActive=False
        userreturn = await self.repository.save(user)
        return {"message":"user is now inactive","user":userreturn}   
    
    async def update_old_user(self, id: int, user_data: UserUpdate):      
        """This function updates an existing user profile in the DB"""
        user = await self.repository.get_by_id(id)

        if not user:
            raise HTTPException(
                status_code=404, 
                detail="User not found"
            )
        
        update_payload = user_data.model_dump(exclude_unset=True)
        user.update_from_dict(update_payload)
        return await self.repository.save(user)
