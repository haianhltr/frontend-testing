from fastapi import APIRouter, HTTPException
from models.decom import Machine, OperationUpdate
from services import decom_service

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
