from fastapi import APIRouter, HTTPException
from backend.models.decom import Machine, OperationUpdate 
from backend.services import decom as decom_service
from backend.core.job_simulator import launch_fake_job, get_job_status  # 👈 NEW
from backend.core.utils.json_loader import load_workflow_definition

router = APIRouter()

@router.get("/machines", response_model=list[Machine])
def get_machines():
    return decom_service.load_data()

@router.post("/machines/{machine_id}/stage/{stage}/op/{operation}/update")
def update_op(machine_id: str, stage: str, operation: str, update: OperationUpdate):
    try:
        decom_service.update_operation(machine_id, stage, operation, update.status)
        return {"message": f"Updated {operation} in {stage} to {update.status}"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Machine/stage/op not found")

@router.post("/machines/random", response_model=Machine)
def add_random_machine():
    return decom_service.add_random_machine()

# ✅ NEW ENDPOINTS
@router.post("/machines/{machine_id}/stage/{stage}/op/{op}/run")
def run_operation(machine_id: str, stage: str, op: str):
    job_id = launch_fake_job(machine_id, stage, op)
    return {"job_id": job_id, "status": "launched"}

@router.get("/jobs/{job_id}")
def check_job(job_id: str):
    return get_job_status(job_id)

@router.post("/machines/{machine_id}/stage/{stage}/run")
def run_stage(machine_id: str, stage: str):
    defs = load_workflow_definition("decom")
    ops = defs.get(stage)

    if not ops:
        raise HTTPException(status_code=404, detail=f"Stage '{stage}' not found")

    results = []
    for op in ops:
        job_id = launch_fake_job(machine_id, stage, op)
        results.append({"operation": op, "job_id": job_id, "status": "launched"})

    return {"stage": stage, "operations": results}