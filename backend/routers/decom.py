from fastapi import APIRouter, HTTPException
from models import Machine, StageUpdate
import json
import time
import json, time, threading, random
from pathlib import Path

router = APIRouter()
DATA_FILE = Path("data/state.json")

STATUSES = ["Not Started", "Running", "Success", "Failed"]

# Load from file or generate 100 machines
def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE) as f:
            return json.load(f)
    else:
        machines = []
        for i in range(1, 101):
            machines.append({
                "id": f"vm-{i:03}",
                "name": f"server-{i}",
                "stages": {
                    "shutdown": "Not Started",
                    "patch_cleanup": "Not Started",
                    "remove_account": "Not Started"
                }
            })
        save_data(machines)
        return machines

def save_data(data):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def update_stage(machine_id, stage, new_status):
    data = load_data()
    for machine in data:
        if machine["id"] == machine_id:
            machine["stages"][stage] = new_status
            save_data(data)
            return
    raise HTTPException(status_code=404, detail="Machine not found")

@router.get("", response_model=list[Machine])
def get_all_machines():
    return load_data()

@router.post("/{machine_id}/stage/{stage}/run")
def run_stage(machine_id: str, stage: str):
    update_stage(machine_id, stage, "Running")

    def simulate_run():
        time.sleep(2)
        from random import choice
        final_status = choice(["Success", "Failed"])
        update_stage(machine_id, stage, final_status)

    threading.Thread(target=simulate_run).start()
    return {"message": f"Stage '{stage}' is now running."}

@router.post("/{machine_id}/stage/{stage}/verify")
def verify_stage(machine_id: str, stage: str, update: StageUpdate):
    if update.status not in STATUSES:
        raise HTTPException(status_code=400, detail="Invalid status")
    update_stage(machine_id, stage, update.status)
    return {"message": f"Stage '{stage}' set to '{update.status}' manually."}

@router.post("/random")
def add_random_machine():
    data = load_data()
    new_id = f"vm-{len(data) + 1:03}"
    new_machine = {
        "id": new_id,
        "name": f"random-server-{len(data) + 1}",
        "stages": {
            "shutdown": random.choice(STATUSES),
            "patch_cleanup": random.choice(STATUSES),
            "remove_account": random.choice(STATUSES),
        }
    }
    data.append(new_machine)
    save_data(data)
    return {"message": f"{new_machine['name']} added."}