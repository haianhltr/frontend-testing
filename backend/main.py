# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from domains.decom.api import router as decom_router  # ✅ NEW import
# from domains.patching.api import router as patching_router
# from domains.incidents.api import router as incidents_router

from core.job_simulator import update_running_jobs
from db.init_db import init_db
import asyncio

app = FastAPI(title="Auto-Remediation Platform")

# ✅ Enable CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ On startup: init DB + start job updater
@app.on_event("startup")
async def startup_event():
    init_db()
    asyncio.create_task(update_running_jobs())

# ✅ Mount routers
app.include_router(decom_router, prefix="/decom", tags=["Decommissioning"])
# app.include_router(patching_router, prefix="/patching", tags=["Patching"])
# app.include_router(incidents_router, prefix="/incidents", tags=["Incidents"])
