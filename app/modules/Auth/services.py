from dotenv import load_dotenv
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from jose import ExpiredSignatureError, JWTError, jwt

from app.config.settings import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    ACCESS_TOKEN_SECRET,
    ALGORITHM,
    REFRESH_TOKEN_EXPIRE_MINUTES,
    REFRESH_TOKEN_SECRET,
)
from app.core.security import (
    create_token,
    verify_password,
)
from app.modules.Auth.repository import AuthRepository
from app.modules.Auth.schema import Login_Schema

load_dotenv()

class Auth_Services:
    """This class contains all the auth services"""

    repository = AuthRepository()

    async def login(self, login_data:Login_Schema):
        """This function is used for login route and create access and refresh token"""
        user = await self.repository.get_user_by_email(login_data.email)

        if(not user or not user.isActive):
            raise HTTPException(status_code=404 , detail="User not found")

        if(not verify_password(user.password , login_data.password)):
            raise HTTPException(status_code=401,detail="Unauthorized")

        data = {"email":login_data.email}

        access_token = create_token(data,ACCESS_TOKEN_EXPIRE_MINUTES,ACCESS_TOKEN_SECRET)

        refresh_token = create_token(data,REFRESH_TOKEN_EXPIRE_MINUTES,REFRESH_TOKEN_SECRET)

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
        """This function is used for refresh route , verifies the refresh token and generate new access token"""
        all_cookies = request.cookies
        refresh_token = all_cookies.get("refreshToken")

        if not refresh_token:
            raise HTTPException(status_code=401, detail="Session expired. Please login again.")

        refresh_token_secret = REFRESH_TOKEN_SECRET
        algorithm = ALGORITHM

        try:
            decoded = jwt.decode(refresh_token,refresh_token_secret,algorithms=[algorithm])
        except ExpiredSignatureError:
            raise HTTPException(status_code=401,detail="Login again") 
        except JWTError :
            raise HTTPException(status_code=401 , detail = "Invalid refresh token")

        email = decoded.get('email')
        user_exists = await self.repository.get_user_by_email(email)
        
        if(not user_exists):
            raise HTTPException(status_code=401,detail="Login again")

        data = {
            "email":decoded.get("email"),
            "name":decoded.get("name")
        }

        access_token = create_token(data , ACCESS_TOKEN_EXPIRE_MINUTES,ACCESS_TOKEN_SECRET)
        response = JSONResponse({"accessToken":access_token},status_code=200)
        return response

    async def logout(self,request:Request):
        """This function is used for login route"""
        refresh_token = request.cookies.get('refreshToken')
        if not refresh_token:
            raise HTTPException(status_code=401, detail="already logged out")

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

