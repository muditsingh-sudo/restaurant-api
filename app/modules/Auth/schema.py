from pydantic import BaseModel, Field


class Login_Schema(BaseModel):
    """This schema validates the incoming user login credentials"""
    email: str = Field(..., max_length=255, min_length=3)
    password: str = Field(..., max_length=225, min_length=8)

class Login_result(BaseModel):
    """This schema defines the structured token response layout after authentication"""
    accessToken: str
    refreshToken: str
