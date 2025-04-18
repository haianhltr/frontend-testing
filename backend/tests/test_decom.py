from fastapi.testclient import TestClient
from main import app
import json

client = TestClient(app)

def test_run_operation():
    machine_id = "vm-test-001"
    stage = "shutdown"
    op = "stop_services"

    response = client.post(f"/decom/machines/{machine_id}/stage/{stage}/op/{op}/run")
    assert response.status_code == 200
    data = response.json()
    assert "job_id" in data
    assert data["status"] == "launched"


#============================
import time

def test_check_job_status():
    machine_id = "vm-test-001"
    stage = "shutdown"
    op = "stop_services"

    # ✅ Fixed: Added /decom prefix
    run_resp = client.post(f"/decom/machines/{machine_id}/stage/{stage}/op/{op}/run")
    job_id = run_resp.json()["job_id"]

    # ✅ Fixed: Added /decom prefix
    status_resp = client.get(f"/decom/jobs/{job_id}")
    assert status_resp.status_code == 200
    assert status_resp.json()["status"] in ["running", "successful"]

    time.sleep(4)
    status_resp = client.get(f"/decom/jobs/{job_id}")
    assert status_resp.json()["status"] == "successful"

def test_run_stage():
    machine_id = "vm-test-001"
    stage = "shutdown"

    res = client.post(f"/decom/machines/{machine_id}/stage/{stage}/run")
    assert res.status_code == 200

    data = res.json()
    assert "stage" in data
    assert data["stage"] == stage

    ops = data.get("operations", [])
    assert len(ops) >= 1
    for op_result in ops:
        assert "operation" in op_result
        assert "job_id" in op_result
        assert op_result["status"] == "launched"


def test_run_all():
    # ✅ Create a machine first
    created = client.post("/decom/machines/random").json()
    machine_id = created["id"]

    res = client.post(f"/decom/machines/{machine_id}/run-all")
    assert res.status_code == 200

    data = res.json()

    print("\n📦 /run-all API Response:\n", json.dumps(data, indent=2), flush=True)

    assert data["machine_id"] == machine_id
    assert data["workflow"] == "decom"
    assert isinstance(data["jobs"], list)
    assert len(data["jobs"]) > 0

    for job in data["jobs"]:
        assert "stage" in job
        assert "operation" in job
        assert "job_id" in job
        assert job["status"] == "launched"

def test_run_all_force():
    # Create a new machine
    created = client.post("/decom/machines/random").json()
    machine_id = created["id"]

    # First run (normal run)
    first_res = client.post(f"/decom/machines/{machine_id}/run-all")
    assert first_res.status_code == 200

    # Wait a bit to let jobs finish
    import time
    time.sleep(4)

    # Run again with force=true
    forced_res = client.post(f"/decom/machines/{machine_id}/run-all?force=true")
    assert forced_res.status_code == 200

    data = forced_res.json()
    print("\n🔁 Forced /run-all Response:\n", json.dumps(data, indent=2), flush=True)

    for job in data["jobs"]:
        assert job["status"] == "launched"  # all ops re-ran
