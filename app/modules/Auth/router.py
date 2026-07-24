from typing import Annotated

from fastapi import APIRouter, Depends, Request

from app.modules.Auth.schema import Login_result, Login_Schema
from app.modules.Auth.services import Auth_Services

authRouter = APIRouter(prefix="/auth",tags=["auth"])

@authRouter.post("/login",response_model=Login_result)
async def login_user(user_detail:Login_Schema,auth_dependency:Annotated[Auth_Services,Depends(Auth_Services)]):
    return await auth_dependency.login(user_detail)

@authRouter.post("/refresh")
async def refresh(request:Request,auth_dependency:Annotated[Auth_Services,Depends(Auth_Services)]):
    return await auth_dependency.refresh(request)

@authRouter.post("/logout")
async def logout(request:Request , auth_dependency:Annotated[Auth_Services,Depends(Auth_Services)]):
    return await auth_dependency.logout(request )
