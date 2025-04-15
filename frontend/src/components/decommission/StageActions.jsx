import React from 'react';

export default function StageActions({ stage, machineId, currentStatus, onUpdate }) {
  const handleRun = () => {
    if (currentStatus === 'Running') return;
    onUpdate(machineId, stage, 'Running');

    setTimeout(() => {
      const success = Math.random() > 0.2;
      onUpdate(machineId, stage, success ? 'Success' : 'Failed');
    }, 2000);
  };

  const handleVerify = () => {
    const newStatus = prompt(
      `Update status for '${stage}' on '${machineId}':`,
      currentStatus
    );
    const valid = ['Not Started', 'Running', 'Success', 'Failed'];
    if (newStatus && valid.includes(newStatus)) {
      onUpdate(machineId, stage, newStatus);
    } else if (newStatus) {
      alert("Invalid status. Valid values: Not Started, Running, Success, Failed");
    }
  };

  return (
    <div style={{ display: 'flex', gap: '5px', marginTop: '5px' }}>
      <button onClick={handleRun} disabled={currentStatus === 'Running'}>
        Run
      </button>
      <button onClick={handleVerify}>Verify</button>
    </div>
  );
}
