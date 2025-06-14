"""
RapidOrch CLI - Command Line Interface for API Integration Orchestrator
"""

import argparse
import sys
from typing import Optional

from loguru import logger

from rapidorch.config import settings


def main() -> None:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="RapidOrch - Adaptive API Integration Orchestrator"
    )
    
    parser.add_argument(
        "--version", 
        action="version", 
        version="RapidOrch 0.9.0"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Server command
    server_parser = subparsers.add_parser("server", help="Start the API server")
    server_parser.add_argument(
        "--host", 
        default="0.0.0.0", 
        help="Host to bind to (default: 0.0.0.0)"
    )
    server_parser.add_argument(
        "--port", 
        type=int, 
        default=8000, 
        help="Port to bind to (default: 8000)"
    )
    server_parser.add_argument(
        "--reload", 
        action="store_true", 
        help="Enable auto-reload for development"
    )
    
    # Status command
    status_parser = subparsers.add_parser("status", help="Check system status")
    
    # Future commands placeholders
    spec_parser = subparsers.add_parser("spec", help="Manage API specifications")
    spec_parser.add_argument("spec_command", choices=["upload", "list", "delete"])
    
    args = parser.parse_args()
    
    if args.command == "server":
        start_server(args.host, args.port, args.reload)
    elif args.command == "status":
        check_status()
    elif args.command == "spec":
        handle_spec_command(args.spec_command)
    else:
        parser.print_help()


def start_server(host: str, port: int, reload: bool) -> None:
    """Start the FastAPI server."""
    try:
        import uvicorn
        logger.info(f"Starting RapidOrch server on {host}:{port}")
        uvicorn.run(
            "rapidorch.main:app",
            host=host,
            port=port,
            reload=reload,
            log_level="info",
        )
    except ImportError:
        logger.error("uvicorn is not installed. Please run: poetry install")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Failed to start server: {e}")
        sys.exit(1)


def check_status() -> None:
    """Check system status."""
    print("🔍 RapidOrch System Status")
    print("=" * 30)
    print(f"Version: 0.9.0")
    print(f"Environment: {settings.environment}")
    print(f"Debug Mode: {settings.debug}")
    print(f"Database URL: {settings.database_url}")
    print(f"Redis URL: {settings.redis_url}")
    print(f"Chroma Host: {settings.chroma_host}:{settings.chroma_port}")
    print(f"OpenAI Model: {settings.openai_model}")
    
    # Check if API key is set
    if settings.openai_api_key:
        print("✅ OpenAI API Key: Configured")
    else:
        print("❌ OpenAI API Key: Not configured")
    
    print("\n🚀 Ready to orchestrate APIs!")


def handle_spec_command(spec_command: str) -> None:
    """Handle spec-related commands."""
    print(f"📋 Spec command: {spec_command}")
    print("⚠️  Spec management will be implemented in Phase 1")
    print("   Stay tuned for spec upload, list, and delete functionality!")


if __name__ == "__main__":
    main() 