# FasterAPI

A production-ready wrapper application framework for FastAPI.

## Features
- Modular Architecture
- Clean Architecture Principles
- Async SQLAlchemy 2.0 Integration
- Generic CRUD
- JWT Authentication & Security

## Installation

```bash
pip install fasterapi
```

## Quick Start

Create a new application:

```python
from fasterapi.core import FasterAPI, FasterAPIConfig, DatabaseConfig

config = FasterAPIConfig(
    title="My App",
    db_config=DatabaseConfig(url="sqlite+aiosqlite:///:memory:")
)

app = FasterAPI(config)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
```

## Real Example

For a complete, production-ready example including authentication, relationships, and custom endpoints, check out the [Simple App Example](examples/simple_app).

This example demonstrates:
- **Custom Models & Schemas**: Using SQLAlchemy models with relationships (User <-> Items).
- **Authentication**: JWT authentication with protected routes.
- **Custom Endpoints**: Advanced filtering and eager loading to prevent N+1 queries.

## Requirements

- Python 3.10+
- FastAPI
- SQLAlchemy 2.0+

