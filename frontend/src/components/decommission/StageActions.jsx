import React from 'react';
import { runStage, verifyStage } from '../../utils/api';

export default function StageActions({ stage, machineId, currentStatus, onUpdate }) {
  const handleRun = async () => {
    if (currentStatus === 'Running') return;
    onUpdate(machineId, stage, 'Running');
    await runStage(machineId, stage);
    // Note: backend auto-updates status after 2s, so frontend can poll if needed
  };

  const handleVerify = async () => {
    const newStatus = prompt(
      `Update status for '${stage}' on '${machineId}':`,
      currentStatus
    );
    const valid = ['Not Started', 'Running', 'Success', 'Failed'];
    if (newStatus && valid.includes(newStatus)) {
      await verifyStage(machineId, stage, newStatus);
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
