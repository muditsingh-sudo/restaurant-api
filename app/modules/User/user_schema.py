from pydantic import BaseModel

class User(BaseModel):
    id: int
    email: str
    name: str
    city: str
    state: str
    zip_code: str
    balance: float

    def __str__(self):
        return f"User(id={self.id},  name={self.name}"