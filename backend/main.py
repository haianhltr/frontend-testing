from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import decom, patching, incidents
from backend.core.config import settings  

app = FastAPI(title="Auto-Remediation Platform")

app = FastAPI(title="Auto-Remediation Platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Mount routers
app.include_router(decom.router, prefix="/decom", tags=["Decommissioning"])
# app.include_router(patching.router, prefix="/patching", tags=["Patching"])
# app.include_router(incidents.router, prefix="/incidents", tags=["Incidents"])
