import React, { useEffect, useState } from 'react';
import MachineTable from '../components/decommission/MachineTable';
import { fetchMachines, addRandomMachine } from '../utils/api';

export default function Decommission() {
  const [machines, setMachines] = useState([]);
  const [resetPage, setResetPage] = useState(false); // ✅ for jumping to last page

  const loadMachines = () => {
    fetchMachines().then(data => {
      console.log("📡 Loaded machines:", data);
      setMachines(data);
    });
  };

  useEffect(() => {
    loadMachines();
  }, []);

  const handleAddMachine = async () => {
    await addRandomMachine();
    loadMachines();
  };



  const updateStageStatus = (machineId, stage, newStatus) => {
    setMachines(prev =>
      prev.map(machine =>
        machine.id === machineId
          ? {
              ...machine,
              stages: { ...machine.stages, [stage]: newStatus },
            }
          : machine
      )
    );
  };

  return (
    <div>
      <h2>🧠 Decom Tracker Dashboard (from API)</h2>
      <button onClick={handleAddMachine} style={{ marginBottom: '1rem' }}>
        ➕ Add Random Machine
      </button>
      <p>Total machines: {machines.length}</p>
      <MachineTable
        machines={machines}
        onUpdate={updateStageStatus}
        resetPage={resetPage}
        setResetPage={setResetPage}
      />
    </div>
  );
}
