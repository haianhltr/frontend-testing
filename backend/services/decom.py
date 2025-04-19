# services/decom.py

import random
import string
from db.session import SessionLocal
from db.crud import (
    get_all_machines,
    get_machine,
    create_machine,
    update_machine_stage_op,
)
from db.models import Machine
from core.utils.json_loader import load_workflow_definition

# Generate a random machine name
def generate_random_name():
    n = random.randint(1, 100)
    return f"random-server-{n:02d}"

# Generate a random machine ID
def generate_random_id():
    return "vm-" + ''.join(random.choices(string.digits, k=3))

# Construct empty stage+operation template from workflow def
def build_stage_structure():
    defs = load_workflow_definition("decom")
    stages = {}
    for stage, ops in defs.items():
        stages[stage] = {
            "operations": {op: "Not Started" for op in ops}
        }
    return stages

# Get all machines from DB
def load_data():
    db = SessionLocal()
    return get_all_machines(db)

# Add a new machine to DB
def add_random_machine():
    db = SessionLocal()
    new_machine = Machine(
        id=generate_random_id(),
        name=generate_random_name(),
        stages=build_stage_structure()
    )
    return create_machine(db, new_machine)

# Update operation status in DB
def update_operation(machine_id: str, stage: str, operation: str, new_status: str):
    db = SessionLocal()
    return update_machine_stage_op(db, machine_id, stage, operation, new_status)
