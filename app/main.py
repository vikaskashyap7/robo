from fastapi import FastAPI
from .routers import configurations
from .database import engine, Base

app = FastAPI()

# Create the database tables
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(configurations.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Configuration Management API"}
