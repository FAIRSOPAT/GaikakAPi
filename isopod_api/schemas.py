from pydantic import BaseModel

class user(BaseModel):
    id : int
    username : str
    password : str
    name : str
    email : str
    phone : str

class user2(BaseModel):
    username : str
    password : str
    name : str
    email : str
    phone : str

class isopodbox(BaseModel):
    Namebox : str
    Typeisopod : str
    Temperature : str
    Humidity : str

class isopodbox2(BaseModel):
    id : int
    Typeisopod : str
    Temperature : str
    Humidity : str
    
class Monitor(BaseModel):
    Name : str
    Size : str
    Age : str
    Detail : str

class Check(BaseModel):
    username : str
    password : str