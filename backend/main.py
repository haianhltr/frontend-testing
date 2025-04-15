from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # ✅ add this
from routers import decom

app = FastAPI(title="Auto-Remediation Backend")

# ✅ CORS configuration to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for now (can restrict later)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include your decom router
app.include_router(decom.router, prefix="/machines")
