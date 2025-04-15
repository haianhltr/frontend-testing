from fastapi import FastAPI
from routers import decom

app = FastAPI(title="Auto-Remediation Backend")

app.include_router(decom.router, prefix="/machines")
