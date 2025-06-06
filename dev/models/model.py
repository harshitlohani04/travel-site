from pydantic import BaseModel

class Hotel(BaseModel):
    hotel_name : str
    location : str
    desc : str
    rooms : int
    lat : float
    long : float


class User(BaseModel):
    firstName : str
    lastName : str
    destination : str
    members : int
    