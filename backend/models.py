from pydantic import BaseModel, EmailStr
class loginuser(BaseModel):
    Email: EmailStr
    password: str