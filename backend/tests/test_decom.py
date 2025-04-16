from fastapi.testclient import TestClient
from backend.main import app


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
