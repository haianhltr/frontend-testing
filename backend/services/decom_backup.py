from db.engine import SessionLocal
from db import crud, models
from core.utils.json_loader import load_workflow_definition

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def load_data():
    db = next(get_db())
    return crud.get_all_machines(db)

def save_data(data):
    db = next(get_db())
    for m in data:
        crud.create_machine(db, m)

def update_operation(machine_id, stage, operation, new_status):
    db = next(get_db())
    result = crud.update_machine_stage_op(db, machine_id, stage, operation, new_status)
    if not result:
        raise ValueError("Update failed")

def add_random_machine():
    db = next(get_db())
    existing = crud.get_all_machines(db)
    new_id = f"vm-{len(existing) + 1:03}"
    new_name = f"random-server-{len(existing) + 1}"

    stages = {
        stage: {"operations": {op: "Not Started" for op in ops}}
        for stage, ops in load_workflow_definition("decom").items()
    }

    machine = models.Machine(id=new_id, name=new_name, stages=stages)
    return crud.create_machine(db, machine)
