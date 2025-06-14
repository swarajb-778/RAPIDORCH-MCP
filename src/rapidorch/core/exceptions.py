"""
Exception handlers for RapidOrch.
"""

from typing import Dict, Any
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from loguru import logger


class RapidOrchException(Exception):
    """Base exception for RapidOrch."""
    
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class SpecIngestionError(RapidOrchException):
    """Exception for spec ingestion errors."""
    
    def __init__(self, message: str):
        super().__init__(message, status_code=400)


class AdapterGenerationError(RapidOrchException):
    """Exception for adapter generation errors."""
    
    def __init__(self, message: str):
        super().__init__(message, status_code=500)


class AuthenticationError(RapidOrchException):
    """Exception for authentication errors."""
    
    def __init__(self, message: str):
        super().__init__(message, status_code=401)


class AuthorizationError(RapidOrchException):
    """Exception for authorization errors."""
    
    def __init__(self, message: str):
        super().__init__(message, status_code=403)


class NotFoundError(RapidOrchException):
    """Exception for not found errors."""
    
    def __init__(self, message: str):
        super().__init__(message, status_code=404)


class RateLimitError(RapidOrchException):
    """Exception for rate limit errors."""
    
    def __init__(self, message: str):
        super().__init__(message, status_code=429)


async def rapidorch_exception_handler(
    request: Request, exc: RapidOrchException
) -> JSONResponse:
    """Handle RapidOrch exceptions."""
    logger.error(f"RapidOrch exception: {exc.message}")
    
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": True,
            "message": exc.message,
            "type": exc.__class__.__name__,
            "status_code": exc.status_code,
        },
    )


async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    """Handle validation exceptions."""
    logger.error(f"Validation error: {exc.errors()}")
    
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": True,
            "message": "Validation error",
            "details": exc.errors(),
            "type": "ValidationError",
            "status_code": 422,
        },
    )


async def general_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """Handle general exceptions."""
    logger.error(f"Unhandled exception: {str(exc)}")
    
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": True,
            "message": "Internal server error",
            "type": "InternalServerError",
            "status_code": 500,
        },
    )


def setup_exception_handlers(app: FastAPI) -> None:
    """Setup exception handlers for the FastAPI app."""
    app.add_exception_handler(RapidOrchException, rapidorch_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(Exception, general_exception_handler) 