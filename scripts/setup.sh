#!/bin/bash
# RapidOrch Development Setup Script

set -e  # Exit on any error

echo "🚀 Setting up RapidOrch development environment..."

# Check if Poetry is installed
if ! command -v poetry &> /dev/null; then
    echo "❌ Poetry is not installed. Please install Poetry first:"
    echo "   curl -sSL https://install.python-poetry.org | python3 -"
    exit 1
fi

# Check Python version
python_version=$(python3 --version | cut -d" " -f2 | cut -d"." -f1,2)
required_version="3.11"

if [[ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]]; then
    echo "❌ Python 3.11 or higher is required. Found: $python_version"
    exit 1
fi

echo "✅ Python version check passed: $python_version"

# Install dependencies
echo "📦 Installing Python dependencies..."
poetry install

# Setup pre-commit hooks
echo "🔧 Setting up pre-commit hooks..."
poetry run pre-commit install

# Copy environment template if .env doesn't exist
if [ ! -f .env ]; then
    echo "📋 Creating .env file from template..."
    cp env.template .env
    echo "⚠️  Please edit .env file and add your API keys and configuration"
fi

# Create necessary directories
echo "📁 Creating necessary directories..."
mkdir -p logs data temp

echo "🐳 To start the development environment:"
echo "   docker-compose up -d"
echo ""
echo "🔧 To run the application locally:"
echo "   poetry run uvicorn rapidorch.main:app --reload"
echo ""
echo "🧪 To run tests:"
echo "   poetry run pytest"
echo ""
echo "✅ Setup complete! Happy coding! 🎉" 