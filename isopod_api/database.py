from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql.cursors
import pymysql

engine = create_engine("mysql+pymysql://phpmyadmin:Isopod123@127.0.0.1:3306/IsopodAPI")
#engine = create_engine("mysql+pymysql://root:@127.0.0.1:3306/isopod")

Session = sessionmaker(bind = engine)
session = Session()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
