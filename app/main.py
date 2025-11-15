from fastapi import FastAPI

app = FastAPI(title="Analytics Service")

@app.get("/")
async def root():
    return {"service": "analytics-service", "status": "running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

