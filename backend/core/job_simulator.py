# backend/core/job_simulator.py

import uuid
import time

job_store = {}

def launch_fake_job(machine_id: str, stage: str, op: str):
    job_id = str(uuid.uuid4())
    job_store[job_id] = {
        "status": "running",
        "start_time": time.time(),
        "machine_id": machine_id,
        "stage": stage,
        "operation": op
    }
    return job_id

def get_job_status(job_id: str):
    job = job_store.get(job_id)
    if not job:
        return {"status": "not_found"}

    if time.time() - job["start_time"] > 3:
        job["status"] = "successful"

    return {"status": job["status"]}
