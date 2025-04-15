const API_BASE = "http://localhost:8000";

export async function fetchMachines() {
  const res = await fetch(`${API_BASE}/machines`);
  return await res.json();
}

export async function runStage(machineId, stage) {
  const res = await fetch(`${API_BASE}/machines/${machineId}/stage/${stage}/run`, {
    method: "POST"
  });
  return await res.json();
}

export async function verifyStage(machineId, stage, status) {
  const res = await fetch(`${API_BASE}/machines/${machineId}/stage/${stage}/verify`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ status })
  });
  return await res.json();
}

export async function addRandomMachine() {
    const res = await fetch("http://localhost:8000/machines/random", {
      method: "POST"
    });
    return await res.json();
  }
