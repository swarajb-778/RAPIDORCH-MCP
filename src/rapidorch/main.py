"""
RapidOrch - Adaptive API Integration Orchestrator
Main FastAPI application entry point.
"""

from contextlib import asynccontextmanager
from typing import Dict, Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from loguru import logger

from rapidorch.config import settings
from rapidorch.core.exceptions import setup_exception_handlers


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager."""
    # Startup
    logger.info("Starting RapidOrch API Integration Orchestrator")
    logger.info(f"Environment: {settings.environment}")
    logger.info(f"Debug mode: {settings.debug}")
    
    yield
    
    # Shutdown
    logger.info("Shutting down RapidOrch")


# Create FastAPI application
app = FastAPI(
    title="RapidOrch",
    description="Adaptive API Integration Orchestrator",
    version="0.9.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup exception handlers
setup_exception_handlers(app)


@app.get("/")
async def root() -> Dict[str, str]:
    """Root endpoint."""
    return {
        "message": "Welcome to RapidOrch - Adaptive API Integration Orchestrator",
        "version": "0.9.0",
        "docs": "/docs",
    }


@app.get("/health")
async def health_check() -> Dict[str, Any]:
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "rapidorch",
        "version": "0.9.0",
        "environment": settings.environment,
    }


@app.get("/v1/status")
async def api_status() -> Dict[str, Any]:
    """API status endpoint."""
    return {
        "api_version": "v1",
        "service": "rapidorch",
        "status": "operational",
        "capabilities": [
            "spec_ingestion",
            "adapter_generation", 
            "workflow_orchestration",
            "auth_management",
            "data_normalization",
        ],
        "endpoints": {
            "specs": "/v1/specs",
            "adapters": "/v1/adapters",
            "workflows": "/v1/workflows",
            "auth": "/v1/auth",
        },
    }


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "rapidorch.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
        log_level="info",
    ) 