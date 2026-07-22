from app.modules.Auth.schema import Login_Schema
from app.modules.User.model import User

from app.core.security import verify_password , create_access_token

from fastapi import HTTPException

class Auth_Services:
    """This class contains all the auth services"""

    def login(self, login_data:Login_Schema):
        user = User.get_or_none(email=login_data.email)

        if(not user or not user.isActive):
            raise HTTPException(status_code=404 , detail="User not found")

        if(not verify_password(user.password , login_data.password)):
            raise HTTPException(status_code=401,detail="Unauthorized")

        access_token = create_access_token(email=login_data.email , name=login_data.name)

        return {"accesstoken":access_token}

        
        

        

