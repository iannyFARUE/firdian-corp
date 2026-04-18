from pydantic import BaseModel, Field, field_validator, model_validator
from typing import List, Optional, Dict

class User(BaseModel):
    id: int
    name: str
    is_active: bool = True
    email: str = Field(..., 
                       pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', 
                       description="The email address of the user")
    age: int = Field(..., gt=0, le=150,description="The age of the user", examples=30)
    username: str

    @field_validator('username')
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
    last_name:str
    first_name: str

    @field_validator('first_name','last_name')
    def names_must_be_capitalize(cls, v):
        if not v.istitle():
            raise ValueError('Names must be capitilized')
        return v


if __name__ == "__main__":
    input = {'id': 1, 'name': 'John Doe', 'is_active': 12}
    # user = User(**input)
    # print(user)
    e = Employee(**{'id':1,'name':'Boss Ian','department':'IT','salary':12000,'last_name':'madhara','first_name':'Ian'})
