import React, { useEffect, useState } from 'react';
import MachineTable from '../components/decommission/MachineTable';
import { fetchMachines } from '../utils/api';

export default function Decommission() {
  const [machines, setMachines] = useState([]);

  useEffect(() => {
    fetchMachines().then(setMachines);
  }, []);

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
      <MachineTable machines={machines} onUpdate={updateStageStatus} />
    </div>
  );
}
