import { useEffect, useState } from "react";
import MachineCard from "../components/decommission/MachineCard";
import { fetchMachines, addRandomMachine } from "../utils/api";
import "../styles/decom.css";



export default function Decommission() {
  const [machines, setMachines] = useState([]);

  useEffect(() => {
    fetchMachines().then(setMachines);
  }, []);

  const handleAddMachine = async () => {
    await addRandomMachine();  // This is from your api.js
    loadMachines();            // This will re-fetch machines
  };
  

  const handleUpdate = (machineId, stage, op, status) => {
    setMachines(prev =>
      prev.map(m =>
        m.id === machineId
          ? {
              ...m,
              stages: {
                ...m.stages,
                [stage]: {
                  operations: {
                    ...m.stages[stage].operations,
                    [op]: status,
                  },
                },
              },
            }
          : m
      )
    );
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
