# backend/utils/json_loader.py

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # Go up to `backend/`

def load_workflow_definition(name: str) -> dict:
    path = BASE_DIR / "workflows" / f"{name}.json"
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)
