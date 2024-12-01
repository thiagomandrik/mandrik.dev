from fastapi import FastAPI

app = FastAPI()

@app.get("/api/")
async def read_root():
    return {"message": 'Backend FastAPI'}
