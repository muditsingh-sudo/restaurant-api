from app.modules.Auth.schema import Login_Schema,Login_result
from app.modules.Auth.services import Auth_Services

from fastapi import APIRouter,  Depends,Request, Response

from typing import Annotated

authRouter = APIRouter(prefix="/auth",tags=["auth"])

@authRouter.post("/login",response_model=Login_result)
async def login_user(user_detail:Login_Schema,Auth_dependency:Annotated[Auth_Services,Depends(Auth_Services)]):
    return await Auth_dependency.login(user_detail)

@authRouter.post("/refresh")
async def refresh(request:Request,Auth_dependency:Annotated[Auth_Services,Depends(Auth_Services)]):
    return await Auth_dependency.refresh(request)

@authRouter.post("/logout")
async def logout(request:Request , Auth_dependency:Annotated[Auth_Services,Depends(Auth_Services)]):
    return await Auth_dependency.logout(request )