# core/utils/json_loader.py
import json
from pathlib import Path

def load_workflow_definition(workflow_name: str):
    path = Path(f"workflows/{workflow_name}.json")
    if not path.exists():
        raise ValueError(f"No definition found for workflow '{workflow_name}'")
    with open(path) as f:
        return json.load(f)
