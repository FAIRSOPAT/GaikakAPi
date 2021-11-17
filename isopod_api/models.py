from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Float
from database import Base
from sqlalchemy.orm import relationship
import datetime, pytz

tz = pytz.timezone('Asia/Bangkok')

class Register(Base):

    __tablename__ = "Register"

    id = Column(Integer,primary_key=True,index=True)
    username = Column(String(100))
    password = Column(String(100))
    name = Column(String(100))
    email = Column(String(100))
    phone = Column(String(100))

class Detailsbox(Base):

    __tablename__ = "Detailsbox"

    id = Column(Integer,primary_key=True,index=True)
    Namebox = Column(String(100))
    Temperature = Column(String(100))
    Humidity = Column(String(100))
    Typeisopod = Column(String(100))
    DateTime = Column(DateTime,default=datetime.datetime.now(tz))

class ShowMonitor(Base):

    __tablename__ = "Monitor"

    id = Column(Integer,primary_key=True,index=True)
    Name = Column(String(100))
    Size = Column(String(100))
    Age = Column(String(100))
    Detail = Column(String(100))
    DateTime = Column(DateTime,default=datetime.datetime.now(tz))

class Imagesave(Base):
    
    __tablename__ = "Imagesave"

    id = Column(Integer,primary_key=True,index=True)
    Namepic = Column(String(100))

class Getdata(Base):
    
    __tablename__ = "Getdata"

    id = Column(Integer,primary_key=True,index=True)
    Temperature = Column(String(100))
    Humidity = Column(String(100))
    Statusfan = Column(String(100))
    Statusfoggy = Column(String(100))