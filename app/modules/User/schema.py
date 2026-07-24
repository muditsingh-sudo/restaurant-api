from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel


class UserBase(BaseModel):
    """Base schema holding shared user fields with model constraints"""
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True  # Allows Pydantic to read Tortoise ORM objects directly
    )

    email: str = Field(..., max_length=255, min_length=3)
    name: str = Field(..., max_length=255, min_length=1)
    city: str = Field(..., max_length=255, min_length=1)
    state: str = Field(..., max_length=255, min_length=1)
    zip_code: str = Field(..., max_length=10, min_length=1)
    balance: Decimal = Field(..., max_digits=12, decimal_places=2, ge=0)
    is_active: bool = Field(default=True, serialization_alias="isActive")


class UserCreate(UserBase):
    """Schema for handling new user registrations"""
    password: str = Field(default="123456789", max_length=225, min_length=8)


class UserUpdate(BaseModel):
    """Schema for executing partial profile modifications"""
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )

    email: str | None = Field(default=None, max_length=255, min_length=3)
    name: str | None = Field(default=None, max_length=255, min_length=1)
    city: str | None = Field(default=None, max_length=255, min_length=1)
    state: str | None = Field(default=None, max_length=255, min_length=1)
    zip_code: str | None = Field(default=None, max_length=10, min_length=1)
    balance: Decimal | None = Field(default=None, max_digits=12, decimal_places=2, ge=0)
    is_active: bool | None = Field(default=None, serialization_alias="isActive")


class UserOut(UserBase):
    """Schema for sanitizing out sensitive user response data"""
    id: int
