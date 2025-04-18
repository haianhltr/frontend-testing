# backend/core/job_simulator.py

import uuid
import time
import random
import asyncio  # ✅ Needed for background task sleep
from services import decom as decom_service

job_store = {}

def launch_fake_job(machine_id: str, stage: str, op: str):
    job_id = str(uuid.uuid4())
    will_fail = random.random() < 0.3  # 💣 30% chance to fail

    job_store[job_id] = {
        "status": "running",
        "start_time": time.time(),
        "machine_id": machine_id,
        "stage": stage,
        "operation": op,
        "will_fail": will_fail,
    }
    return job_id

def get_job_status(job_id: str):
    job = job_store.get(job_id)
    if not job:
        return {"status": "not_found"}

    if time.time() - job["start_time"] > 3:
        if job["status"] == "running":
            if job.get("will_fail"):
                job["status"] = "failed"
                try:
                    decom_service.update_operation(
                        machine_id=job["machine_id"],
                        stage=job["stage"],
                        operation=job["operation"],
                        new_status="Failed"
                    )
                except Exception as e:
                    print(f"⚠️ Failed to update Failed status: {e}", flush=True)
            else:
                job["status"] = "successful"
                try:
                    decom_service.update_operation(
                        machine_id=job["machine_id"],
                        stage=job["stage"],
                        operation=job["operation"],
                        new_status="Success"
                    )
                except Exception as e:
                    print(f"⚠️ Failed to update Success status: {e}", flush=True)

    return {"status": job["status"]}


# ✅ Background task that runs every 5s
async def update_running_jobs():
    while True:
        for job_id, job in list(job_store.items()):
            if job["status"] == "running":
                get_job_status(job_id)  # This will auto-mark as Success/Failed
        await asyncio.sleep(5)
