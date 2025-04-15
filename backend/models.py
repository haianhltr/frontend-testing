from pydantic import BaseModel

class Machine(BaseModel):
    id: str
    name: str
    stages: dict

class StageUpdate(BaseModel):
    status: str
