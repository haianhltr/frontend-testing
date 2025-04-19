# domains/decom/crud.py

from sqlalchemy.orm import Session
from .models import Machine


def get_all(db: Session):
    return db.query(Machine).all()

def get_one(db: Session, machine_id: str):
    return db.query(Machine).filter(Machine.id == machine_id).first()

def create(db: Session, machine: Machine):
    db.add(machine)
    db.commit()
    db.refresh(machine)
    return machine

def update_op_status(db: Session, machine_id: str, stage: str, op: str, new_status: str):
    machine = get_one(db, machine_id)
    if not machine:
        return None

    data = machine.stages
    if stage in data and op in data[stage]["operations"]:
        data[stage]["operations"][op] = new_status
        machine.stages = data
        db.commit()
        db.refresh(machine)
        return machine

    return None
