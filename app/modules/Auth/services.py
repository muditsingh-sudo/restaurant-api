from app.modules.Auth.schema import Login_Schema
from app.modules.User.model import User

from app.core.security import verify_password , create_access_token,create_refresh_token

from fastapi import HTTPException,Request, Response
from fastapi.responses import JSONResponse

from dotenv import load_dotenv

from jose import ExpiredSignatureError, jwt

import os

load_dotenv()

class Auth_Services:
    """This class contains all the auth services"""

    async def login(self, login_data:Login_Schema):
        user = await User.get_or_none(email=login_data.email)

        if(not user or not user.isActive):
            raise HTTPException(status_code=404 , detail="User not found")

        if(not verify_password(user.password , login_data.password)):
            raise HTTPException(status_code=401,detail="Unauthorized")

        data = {"email":login_data.email,"name":login_data.name}

        access_token = create_access_token(data)

        refresh_token = create_refresh_token(data)

        response = JSONResponse({"accessToken":access_token},status_code=200)
        response.set_cookie(
                        key="refreshToken",
                        value=refresh_token,
                        httponly=True,
                        secure=False,       
                        samesite="lax",     
                        path="/"            
                    )

        return response

    async def refresh(self,request:Request):
        
        all_cookies = request.cookies
        refresh_token = all_cookies.get("refreshToken")

        if not refresh_token:
            raise HTTPException(status_code=401, detail="Session expired. Please login again.")

        refresh_token_secret = os.getenv("REFRESH_TOKEN_SECRET")
        algorithm = os.getenv("ALGORITHM")

        try:
            decoded = jwt.decode(refresh_token,refresh_token_secret,algorithms=[algorithm])
        except ExpiredSignatureError:
            raise HTTPException(status_code=401,detail="Login again") 

        email = decoded.get('email')
        user_exists = await User.get_or_none(email=email)
        
        if(not user_exists):
            raise HTTPException(status_code=401,detail="Login again")

        data = {
            "email":decoded.get("email"),
            "name":decoded.get("name")
        }

        access_token = create_access_token(data)
        response = JSONResponse({"accessToken":access_token},status_code=200)
        return response

    async def logout(self,request:Request):
        refresh_token = request.cookies.get('refreshToken')
        if not refresh_token:
            raise HTTPException(status_code=401, detail="all ready logged out")

        response = JSONResponse(content={"detail": "Successfully logged out"},status_code=200)
                                
        response.delete_cookie(
            key="refreshToken",
            path="/",             
            domain=None,          
            httponly=True,     
            secure=False,          
            samesite="lax"         
        )
    
        return response

