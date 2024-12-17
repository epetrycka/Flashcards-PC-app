from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    fullname: str
    nickname: str
    name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True
