# RapidOrch - Adaptive API Integration Orchestrator

**Version**: 0.9 (Development)
**Status**: ✅ Successfully connected to GitHub!

## Vision

RapidOrch provides developers and AI agents with a "universal API layer" that can:
- Ingest any OpenAPI or GraphQL spec at run-time
- Instantly expose normalized, type-safe adapters  
- Keep adapters up-to-date as specs evolve
- Reduce "time-to-first-call" for new external APIs from days/weeks to < 5 minutes

## Quick Start

```bash
# Clone and setup
git clone https://github.com/swarajb-778/RAPIDORCH-MCP.git
cd RapidOrch
docker-compose up -d
```

## Architecture

- **Gateway API** (FastAPI) - Main REST endpoints
- **Spec Ingestion Service** - Validates/parses OpenAPI & GraphQL
- **Adapter Generator** - LLM-driven code generation
- **Auth Manager** - OAuth 2, API-Key, Basic auth flows
- **Normalization Engine** - Field mapping and transformation
- **Workflow Orchestrator** - Chained calls with dependency graphs

## Development Status

**Phase 0 - Bootstrap** ✅ **COMPLETED**

- [x] Project structure setup
- [x] Docker baseline (Python 3.11-slim, uvicorn, poetry)
- [x] CI/CD pipeline (GitHub Actions)
- [x] FastAPI base service ("Hello World")
- [x] LLM provider decision (OpenAI GPT-4)
- [x] Pre-commit hooks and coding standards
- [x] Testing framework setup

**Ready for Phase 1 - Spec Ingestion MVP**

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines.

## License

[Add license information]
