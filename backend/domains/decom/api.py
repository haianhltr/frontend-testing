# domains/decom/api.py
from fastapi import APIRouter, HTTPException, Query
from core.job_simulator import launch_fake_job, get_job_status
from utils.json_loader import load_workflow_definition
from .schemas import Machine, OperationUpdate
from .service import DecomService

router = APIRouter()
service = DecomService()

@router.get("/machines", response_model=list[Machine])
def get_all():
    return service.get_all_machines()

@router.post("/machines/random", response_model=Machine)
def add():
    return service.create_random_machine()

@router.post("/machines/{machine_id}/stage/{stage}/op/{op}/run")
def run_op(machine_id: str, stage: str, op: str):
    job_id = launch_fake_job(machine_id, stage, op)
    updated = service.update_operation(machine_id, stage, op, "Running")
    if not updated:
        raise HTTPException(status_code=404, detail="Operation not found")
    return {"job_id": job_id, "status": "launched"}

@router.post("/machines/{machine_id}/stage/{stage}/op/{op}/update")
def update_op(machine_id: str, stage: str, op: str, update: OperationUpdate):
    success = service.update_operation(machine_id, stage, op, update.status)
    if not success:
        raise HTTPException(status_code=404, detail="Failed to update operation")
    return {"message": f"{op} set to {update.status}"}

@router.get("/jobs/{job_id}")
def check_job(job_id: str):
    return get_job_status(job_id)

@router.get("/machines/status-summary")
def get_summary():
    all_machines = service.get_all_machines()
    result = []
    for m in all_machines:
        summary = {"Success": 0, "Running": 0, "Failed": 0, "Not Started": 0}
        for stage in m.stages.values():
            for status in stage["operations"].values():
                if status in summary:
                    summary[status] += 1
        result.append({"id": m.id, "name": m.name, "summary": summary})
    return result

@router.post("/machines/{machine_id}/stage/{stage}/run")
def run_stage(machine_id: str, stage: str):
    ops = load_workflow_definition("decom").get(stage)
    if not ops:
        raise HTTPException(status_code=404, detail="Stage not found")

    results = []
    for op in ops:
        job_id = launch_fake_job(machine_id, stage, op)
        service.update_operation(machine_id, stage, op, "Running")
        results.append({"operation": op, "job_id": job_id, "status": "launched"})

    return {"stage": stage, "operations": results}

@router.post("/machines/{machine_id}/run-all")
def run_all(machine_id: str, force: bool = Query(False)):
    workflow = load_workflow_definition("decom")
    machine = service.get_machine(machine_id)
    if not machine:
        raise HTTPException(status_code=404, detail="Machine not found")

    results = []
    for stage, ops in workflow.items():
        for op in ops:
            current = machine.stages.get(stage, {}).get("operations", {}).get(op, "Not Started")

            if not force and current == "Success":
                results.append({
                    "stage": stage,
                    "operation": op,
                    "skipped": True,
                    "status": current
                })
                continue

            job_id = launch_fake_job(machine_id, stage, op)
            service.update_operation(machine_id, stage, op, "Running")

            results.append({
                "stage": stage,
                "operation": op,
                "job_id": job_id,
                "status": "launched"
            })

    return {"machine_id": machine_id, "workflow": "decom", "jobs": results}
