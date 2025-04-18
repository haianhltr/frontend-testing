from fastapi import APIRouter, HTTPException
from models.decom import Machine, OperationUpdate
from services import decom as decom_service
from core.job_simulator import launch_fake_job, get_job_status
from core.utils.json_loader import load_workflow_definition
from fastapi import Query

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

#=================================================================
@router.post("/machines/{machine_id}/stage/{stage}/op/{op}/run")
def run_operation(machine_id: str, stage: str, op: str):
    job_id = launch_fake_job(machine_id, stage, op)

    # ✅ Immediately set status to "Running"
    machines = decom_service.load_data()
    for m in machines:
        if m.id == machine_id:
            m.stages[stage].operations[op] = "Running"
            break
    decom_service.save_data(machines)

    return {"job_id": job_id, "status": "launched"}

#=================================================================


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

@router.post("/machines/{machine_id}/run-all")
def run_all(machine_id: str, force: bool = Query(False)):
    from core.utils.json_loader import load_workflow_definition

    defs = load_workflow_definition("decom")  # e.g. shutdown → [op1, op2]
    machines = decom_service.load_data()

    # Find the machine
    machine = next((m for m in machines if m.id == machine_id), None)
    if not machine:
        raise HTTPException(status_code=404, detail="Machine not found")

    results = []

    for stage, ops in defs.items():
        for op in ops:
            current_status = machine.stages[stage].operations.get(op, "Not Started")

            # ✅ Skip successful operations unless forced
            if not force and current_status == "Success":
                results.append({
                    "stage": stage,
                    "operation": op,
                    "skipped": True,
                    "status": current_status
                })
                continue

            # Launch the job
            job_id = launch_fake_job(machine_id, stage, op)

            # ✅ Update the status in the machine object
            machine.stages[stage].operations[op] = "Running"

            results.append({
                "stage": stage,
                "operation": op,
                "job_id": job_id,
                "status": "launched"
            })

    # ✅ Save updated machine state
    decom_service.save_data(machines)

    return {
        "machine_id": machine_id,
        "workflow": "decom",
        "jobs": results
    }

@router.get("/machines/status-summary")
def get_status_summary():
    machines = decom_service.load_data()
    result = []

    for m in machines:
        summary = {
            "Success": 0,
            "Running": 0,
            "Failed": 0,
            "Not Started": 0
        }

        for stage in m.stages.values():
            for status in stage.operations.values():
                if status in summary:
                    summary[status] += 1

        result.append({
            "id": m.id,
            "name": m.name,
            "summary": summary
        })

    return result
