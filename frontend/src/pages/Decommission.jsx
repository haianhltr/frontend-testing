import { useEffect, useState } from "react";
import MachineCard from "../components/decommission/MachineCard";
import { fetchMachines, addRandomMachine } from "../utils/api";
import "../styles/decom.css";

export default function Decommission() {
  const [machines, setMachines] = useState([]);

  const loadMachines = async () => {
    const data = await fetchMachines();
    setMachines(data);
  };

  useEffect(() => {
    loadMachines();
  }, []);

  const handleAddMachine = async () => {
    await addRandomMachine();
    await loadMachines(); // ✅ Refresh list after adding
  };

  const handleUpdate = async () => {
    await loadMachines(); // ✅ Refresh after retry
  };

  return (
    <div>
      <h2>🧠 Decommission Tracker</h2>
      <button className="add-btn" onClick={handleAddMachine}>➕ Add Machine</button>

      {machines.map(m => (
        <MachineCard key={m.id} machine={m} onUpdate={handleUpdate} />
      ))}
    </div>
  );
}
