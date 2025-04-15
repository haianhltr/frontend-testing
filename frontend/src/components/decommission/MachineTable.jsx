import React from 'react';
import StatusBadge from '../common/StatusBadge';
import StageActions from './StageActions';

const stages = ['shutdown', 'patch_cleanup', 'remove_account'];

export default function MachineTable({ machines, onUpdate }) {
  return (
    <table border="1" cellPadding="10" cellSpacing="0">
      <thead>
        <tr>
          <th>Machine</th>
          {stages.map(stage => (
            <th key={stage}>{stage.replace('_', ' ')}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {machines.map(machine => (
          <tr key={machine.id}>
            <td>{machine.name}</td>
            {stages.map(stage => (
              <td key={stage}>
                <StatusBadge status={machine.stages[stage]} />
                <StageActions
                  stage={stage}
                  machineId={machine.id}
                  currentStatus={machine.stages[stage]}
                  onUpdate={onUpdate}
                />
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}
