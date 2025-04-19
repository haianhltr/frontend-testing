# domains/decom/__init__.py

"""
Domain: Decommissioning

Contains all logic, models, and API endpoints related to the 'decom' workflow,
including machine registration, staged operation tracking, and job execution.

Modules:
- api.py        → FastAPI router with all decom endpoints
- service.py    → Business logic layer
- crud.py       → DB interaction logic (SQLAlchemy)
- models.py     → SQLAlchemy model for the 'machines' table
- schema.py     → Pydantic schemas for request/response
"""
