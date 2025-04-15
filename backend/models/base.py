from pydantic import BaseModel
from typing import Dict

class Stage(BaseModel):
    operations: Dict[str, str]  # ✅ Replace OperationStatus with str

class MachineBase(BaseModel):
    id: str
    name: str
