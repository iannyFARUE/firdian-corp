from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool = True


if __name__ == "__main__":
    input = {'id': 1, 'name': 'John Doe', 'is_active': 12}
    user = User(**input)
    print(user)
