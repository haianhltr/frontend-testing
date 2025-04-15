import React, { useState } from 'react';
import MachineTable from '../components/decommission/MachineTable';

const statuses = ['Not Started', 'Running', 'Success', 'Failed'];

const getRandomStatus = () => {
  return statuses[Math.floor(Math.random() * statuses.length)];
};

const generateMockMachines = (count) => {
  return Array.from({ length: count }, (_, i) => ({
    id: `vm-${String(i + 1).padStart(3, '0')}`,
    name: `server-${i + 1}`,
    stages: {
      shutdown: getRandomStatus(),
      patch_cleanup: getRandomStatus(),
      remove_account: getRandomStatus(),
    },
  }));
};

export default function Decommission() {
  const [machines, setMachines] = useState(generateMockMachines(100));

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
      <h2>🧠 Decom Tracker Dashboard (100 Machines)</h2>
      <MachineTable machines={machines} onUpdate={updateStageStatus} />
    </div>
  );
}
