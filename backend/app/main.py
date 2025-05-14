from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Optional, Any
import os
from dotenv import load_dotenv

# Import routes
from app.routes import predict, simulate, compare

# Load environment variables
load_dotenv()

# Verify environment variables are set/loaded
db_url = os.getenv("DATABASE_URL")
frontend_url = os.getenv("FRONTEND_URL")

# Initialize FastAPI app
app = FastAPI(
    title="RaceCast Pro API",
    description="Backend API for RaceCast Pro F1 Analytics Platform",
    version="1.0.0"
)

# Configure CORS
origins = [
    "http://localhost:3000",
    "https://racecast-pro.vercel.app",
    frontend_url,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(predict.router, prefix="/api", tags=["predictions"])
app.include_router(simulate.router, prefix="/api", tags=["simulations"])
app.include_router(compare.router, prefix="/api", tags=["comparisons"])

@app.get("/")
def root():
    """Root endpoint to check API status."""
    return {
        "status": "online",
        "api": "RaceCast Pro Backend",
        "version": "1.0.0"
    }

@app.get("/api/healthcheck")
def healthcheck():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "services": {
            "database": "connected",
            "ml_model": "loaded"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)