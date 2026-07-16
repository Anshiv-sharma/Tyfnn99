from pydantic import BaseModel , EmailStr

class UserCreate(BaseModel):
    name: str
    email: Emailstr
    phone: str
    password: str