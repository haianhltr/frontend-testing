# tests/test_job_simulator.py

import time
from core import job_simulator

def test_simulated_success():
    job_id = job_simulator.launch_fake_job("vm-001", "shutdown", "stop_services")
    assert job_simulator.get_job_status(job_id)["status"] == "running"

    time.sleep(3.1)
    status = job_simulator.get_job_status(job_id)["status"]
    assert status in ["successful", "failed"]  # due to 30% failure logic

def test_running_before_timeout():
    job_id = job_simulator.launch_fake_job("vm-001", "shutdown", "stop_services")
    status = job_simulator.get_job_status(job_id)["status"]
    assert status == "running"  # Should not flip early

def test_simulated_failure():
    # Force a job with failure for deterministic test
    job_id = job_simulator.launch_fake_job("vm-001", "shutdown", "stop_services")
    job_simulator.job_store[job_id]["will_fail"] = True
    time.sleep(3.1)

    status = job_simulator.get_job_status(job_id)["status"]
    assert status == "failed"


# docker-compose run --rm test pytest tests/test_job_simulator.py -s
# docker-compose run --rm test pytest -s
