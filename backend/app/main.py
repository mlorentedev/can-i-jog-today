import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "The backend is running!"}

def run():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
