from fastapi import FastAPI

app = FastAPI(
    title="NextGen Data Engineering Platform Gateway",
    description="API Gateway for the NextGen Data Engineering Platform",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to NextGen Data Engineering Platform",
        "status": "running",
    }