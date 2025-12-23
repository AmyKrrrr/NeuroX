from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # <--- 1. Import this
from app.api.routes import router

app = FastAPI(title="Agentic Research Platform")

# 2. Add this block to allow React to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/health")
async def health():
    return {"status": "ok"}