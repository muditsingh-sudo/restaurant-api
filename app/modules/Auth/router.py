from app.modules.Auth.schema import Login_Schema
from app.modules.Auth.services import Auth_Services

from fastapi import APIRouter,  Depends

from typing import Annotated

router = APIRouter(prefix="/auth",tags=["auth"])

@router.get("/login" )
async def login_user(user_detail:Login_Schema,Auth_dependency:Annotated[Auth_Services,Depends(Auth_Services)]):
    return await Auth_dependency.login(user_detail)
