from pydantic import BaseModel
from typing import Dict

class Stage(BaseModel):
    operations: Dict[str, str]

class MachineBase(BaseModel):
    id: str
    name: str

class Machine(MachineBase):
    stages: Dict[str, Stage]

class OperationUpdate(BaseModel):
    status: str
