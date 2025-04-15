from pydantic import BaseModel
from typing import Dict
from models.base import MachineBase, Stage

class Machine(MachineBase):
    stages: Dict[str, Stage]

class OperationUpdate(BaseModel):
    status: str