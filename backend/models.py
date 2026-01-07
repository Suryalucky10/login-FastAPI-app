from pydantic import BaseModel, EmailStr
class loginuser(BaseModel):
    email: EmailStr
    password: str
