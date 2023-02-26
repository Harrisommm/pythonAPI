from fastapi import FastAPI

app = FastAPI()


@app.get("/") 
async def root():
    return {"message": "Welcome to my first API server"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}