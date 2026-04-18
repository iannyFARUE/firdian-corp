from pydantic import BaseModel, Field, field_validator, model_validator
from typing import List, Optional, Dict

class User(BaseModel):
    id: int
    name: str
    is_active: bool = True
    email: str = Field(..., 
                       regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', 
                       description="The email address of the user")
    age: int = Field(..., gt=0, le=150,description="The age of the user", examples=30)
    username: str

    @field_validator
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be atleast 4 characters")
        return v


class SignUpDatat(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("Password do not match")
        return values

class Employee(BaseModel):
    id: int
    name: str = Field(..., description="The name of the employee", min_length=3, max_length=50, examples="Ian Madhara")
    department: Optional[str] = 'General'
    salary : float = Field(..., gt=1000, description="The salary of the employee", examples=50000.00)


if __name__ == "__main__":
    input = {'id': 1, 'name': 'John Doe', 'is_active': 12}
    user = User(**input)
    print(user)
