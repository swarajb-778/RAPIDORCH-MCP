"""
Configuration settings for RapidOrch.
"""

from typing import List, Optional
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""
    
    # App settings
    environment: str = Field(default="development", description="Environment name")
    debug: bool = Field(default=True, description="Debug mode")
    log_level: str = Field(default="INFO", description="Logging level")
    
    # API settings
    api_title: str = Field(default="RapidOrch", description="API title")
    api_version: str = Field(default="0.9.0", description="API version")
    allowed_origins: List[str] = Field(
        default=["http://localhost:3000", "http://localhost:8000"],
        description="Allowed CORS origins"
    )
    
    # Database settings
    database_url: Optional[str] = Field(
        default="postgresql://rapidorch:rapidorch@localhost:5432/rapidorch",
        description="Database connection URL"
    )
    
    # Redis settings
    redis_url: Optional[str] = Field(
        default="redis://localhost:6379/0",
        description="Redis connection URL"
    )
    
    # Chroma settings
    chroma_host: str = Field(default="localhost", description="Chroma host")
    chroma_port: int = Field(default=8001, description="Chroma port")
    
    # LLM settings
    openai_api_key: Optional[str] = Field(default=None, description="OpenAI API key")
    openai_model: str = Field(default="gpt-4", description="OpenAI model name")
    max_tokens: int = Field(default=2000, description="Max tokens for LLM responses")
    
    # Security settings
    secret_key: str = Field(
        default="your-secret-key-change-in-production",
        description="Secret key for JWT tokens"
    )
    algorithm: str = Field(default="HS256", description="JWT algorithm")
    access_token_expire_minutes: int = Field(
        default=30, description="Access token expiration in minutes"
    )
    
    # Rate limiting
    rate_limit_requests: int = Field(default=100, description="Rate limit requests per minute")
    rate_limit_window: int = Field(default=60, description="Rate limit window in seconds")
    
    class Config:
        env_file = ".env"
        env_prefix = "RAPIDORCH_"
        case_sensitive = False


# Global settings instance
settings = Settings() 