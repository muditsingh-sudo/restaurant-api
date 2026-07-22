from pydantic import BaseModel

class Login_Schema(BaseModel):
    email:str
    name:str
    password:str