from pydantic import BaseModel, Field


class create_restaurant_schema(BaseModel):
    name: str = Field(..., max_length=255, min_length=1)
    city: str = Field(..., max_length=255, min_length=1)
    state: str = Field(..., max_length=255, min_length=1)
    zip_code: str = Field(..., max_length=10, min_length=1)
    owner_id: int

class add_menu_schema(BaseModel):
    name: str = Field(..., max_length=255, min_length=1)
    info: str
    price: int = Field(..., gte=0)
    availability: int = Field(..., gte=0)

class assing_owner_schema(BaseModel):
    user_id: int
    restaurant_id: int

class menu_update(BaseModel):
    name: str | None = Field(default=None, max_length=255, min_length=1)
    info: str | None = None
    price: int | None = Field(default=None, gte=0)
    availability: int | None = Field(default=None, gte=0)
 