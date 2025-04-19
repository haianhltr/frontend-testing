# domains/decom/service.py

import random
import string
from sqlalchemy.orm import Session
from db.session import SessionLocal
from . import crud
from .models import Machine
from utils.json_loader import load_workflow_definition



class DecomService:
    def __init__(self):
        self.db: Session = SessionLocal()

    def generate_random_name(self):
        n = random.randint(1, 100)
        return f"random-server-{n:02d}"

    def generate_random_id(self):
        return "vm-" + ''.join(random.choices(string.digits, k=3))

    def build_stage_structure(self):
        defs = load_workflow_definition("decom")
        return {
            stage: {"operations": {op: "Not Started" for op in ops}}
            for stage, ops in defs.items()
        }

    def get_all_machines(self):
        return crud.get_all(self.db)

    def get_machine(self, machine_id: str):
        return crud.get_one(self.db, machine_id)

    def create_random_machine(self):
        machine = Machine(
            id=self.generate_random_id(),
            name=self.generate_random_name(),
            stages=self.build_stage_structure()
        )
        return crud.create(self.db, machine)

    def update_operation(self, machine_id: str, stage: str, op: str, status: str) -> bool:
        result = crud.update_op_status(self.db, machine_id, stage, op, status)
        return result is not None
