from pydantic import BaseModel, computed_field,Field

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(...,ge=1)
    rate_per_night: float

    @computed_field
    @property
    def total_amount(self)->float:
        return self.rate_per_night * self.nights
    
if __name__ == "__main__":
    input = {'id':1,'room_id':1,'nights':2,'rate_per_night':3}
    b1 = Booking(**{'user_id':1,'room_id':1,'nights':2,'rate_per_night':3})
    print(b1.total_amount)
    print(b1.model_dump())