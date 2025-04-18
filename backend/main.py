from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import decom
# from routers import patching, incidents
from core.config import settings
from core.job_simulator import update_running_jobs  # ✅ Import the updater
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

# ✅ Start background loop when app starts
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(update_running_jobs())  # 🔁 Background checker

# ✅ Mount your routers
app.include_router(decom.router, prefix="/decom", tags=["Decommissioning"])
# app.include_router(patching.router, prefix="/patching", tags=["Patching"])
# app.include_router(incidents.router, prefix="/incidents", tags=["Incidents"])
