from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models
from .database import engine
from .routers import user, post, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='l', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print("Connection failed")
        print("Error: ", error)
        time.sleep(3)

app.include_router(post.router)
app.include_router(user.router) 
app.include_router(auth.router)

@app.get("/") 
async def root():
    return {"message": "Welcome to my first API server"}