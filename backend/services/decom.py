import json
from pathlib import Path
from typing import List
from backend.models.decom import Machine 
from backend.core.utils.json_loader import load_workflow_definition

DATA_FILE = Path("data/decom.json")

def load_data() -> List[Machine]:
    if DATA_FILE.exists():
        with open(DATA_FILE) as f:
            return [Machine(**m) for m in json.load(f)]
    return []

def save_data(data: List[Machine]):
    with open(DATA_FILE, "w") as f:
        json.dump([m.dict() for m in data], f, indent=2)

def update_operation(machine_id: str, stage: str, operation: str, new_status: str):
    data = load_data()
    for m in data:
        if m.id == machine_id:
            if stage in m.stages and operation in m.stages[stage]["operations"]:
                m.stages[stage]["operations"][operation] = new_status
                save_data(data)
                return
    raise ValueError("Machine or operation not found")

def create_blank_machine(machine_id: str, name: str) -> Machine:
    defs = load_workflow_definition("decom")
    stages = {
        stage: {"operations": {op: "Not Started" for op in ops}}
        for stage, ops in defs.items()
    }
    return Machine(id=machine_id, name=name, stages=stages)

def add_random_machine():
    data = load_data()
    new_id = f"vm-{len(data) + 1:03}"
    new_name = f"random-server-{len(data) + 1}"
    new_machine = create_blank_machine(new_id, new_name)
    data.append(new_machine)
    save_data(data)
    return new_machine
