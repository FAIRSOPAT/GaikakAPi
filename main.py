from fastapi import FastAPI, Depends, status, Response, HTTPException
from typing import List
from . import models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

@app.post("/Register")
def create_account():
    pass
