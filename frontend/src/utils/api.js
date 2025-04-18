const API_BASE = "http://localhost:8000/decom";

export async function fetchMachines() {
  const res = await fetch(`${API_BASE}/machines`);
  return await res.json();
}

export async function addRandomMachine() {
  const res = await fetch(`${API_BASE}/machines/random`, { method: "POST" });
  return await res.json();
}

export async function updateOperation(machineId, stage, op, status) {
  const res = await fetch(`${API_BASE}/machines/${machineId}/stage/${stage}/op/${op}/update`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ status }),
  });
  return await res.json();
}

export async function retryOperation(machineId, stage, op) {
  const res = await fetch(`${API_BASE}/machines/${machineId}/stage/${stage}/op/${op}/run`, {
    method: "POST",
  });
  return await res.json();
}
