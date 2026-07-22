from decimal import Decimal

from pydantic import BaseModel, Field

class User(BaseModel):
    email: str
    name: str
    city: str
    state: str
    zip_code: str
    balance: Decimal = Field(..., max_digits=12, decimal_places=2)
    isActive: bool

class UserCreate(User):
    password:str

class UserUpdate(BaseModel):
    email: str | None = None
    name: str | None = None
    city: str | None = None
    state: str | None = None
    zip_code: str | None = None
    balance: Decimal |None = Field(default=None, max_digits=12, decimal_places=2)
    isActive:bool | None = None

class UserOut(User):
    id:int
    pass

