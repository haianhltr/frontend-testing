from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import decom, patching, incidents
from core.config import settings  # optional, for environment config

app = FastAPI(title="Auto-Remediation Platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In prod, lock this down
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount routers
app.include_router(decom.router, prefix="/decom", tags=["Decommissioning"])
# app.include_router(patching.router, prefix="/patching", tags=["Patching"])
# app.include_router(incidents.router, prefix="/incidents", tags=["Incidents"])
