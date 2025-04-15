import React, { useState } from 'react';
import MachineTable from '../components/decommission/MachineTable';

export default function Decommission() {
  const [machines, setMachines] = useState([
    {
      id: 'vm-001',
      name: 'finance-server-1',
      stages: {
        shutdown: 'Not Started',
        patch_cleanup: 'Not Started',
        remove_account: 'Not Started',
      },
    },
    {
      id: 'vm-002',
      name: 'web-server-22',
      stages: {
        shutdown: 'Success',
        patch_cleanup: 'Failed',
        remove_account: 'Not Started',
      },
    },
  ]);

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
      <h2>🧠 Decom Tracker Dashboard</h2>
      <MachineTable machines={machines} onUpdate={updateStageStatus} />
    </div>
  );
}
