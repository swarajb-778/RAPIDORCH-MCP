"""
Tests for the main FastAPI application.
"""

import pytest
from fastapi.testclient import TestClient

from rapidorch.main import app

client = TestClient(app)


def test_root_endpoint():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Welcome to RapidOrch - Adaptive API Integration Orchestrator"
    assert data["version"] == "0.9.0"
    assert data["docs"] == "/docs"


def test_health_check():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "rapidorch"
    assert data["version"] == "0.9.0"
    assert "environment" in data


def test_api_status():
    """Test the API status endpoint."""
    response = client.get("/v1/status")
    assert response.status_code == 200
    data = response.json()
    assert data["api_version"] == "v1"
    assert data["service"] == "rapidorch"
    assert data["status"] == "operational"
    assert "capabilities" in data
    assert "spec_ingestion" in data["capabilities"]
    assert "adapter_generation" in data["capabilities"]
    assert "endpoints" in data


def test_openapi_docs():
    """Test that OpenAPI docs are accessible."""
    response = client.get("/docs")
    assert response.status_code == 200


def test_openapi_json():
    """Test that OpenAPI JSON is accessible."""
    response = client.get("/openapi.json")
    assert response.status_code == 200
    data = response.json()
    assert data["info"]["title"] == "RapidOrch"
    assert data["info"]["version"] == "0.9.0" 