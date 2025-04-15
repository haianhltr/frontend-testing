import React, { useState, useEffect } from 'react';
import StatusBadge from '../common/StatusBadge';
import StageActions from './StageActions';

const stages = ['shutdown', 'patch_cleanup', 'remove_account'];
const PAGE_SIZE = 10;

export default function MachineTable({ machines, onUpdate, resetPage, setResetPage }) {
  const totalPages = Math.ceil(machines.length / PAGE_SIZE);
  const [page, setPage] = useState(1);

  useEffect(() => {
    if (resetPage) {
      setPage(totalPages);     // ✅ jump to last page
      setResetPage(false);     // ✅ reset flag
    }
  }, [machines.length, resetPage, totalPages, setResetPage]);

  const paginated = machines.slice((page - 1) * PAGE_SIZE, page * PAGE_SIZE);

  return (
    <div>
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
          {paginated.map(machine => (
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

      <div style={{ marginTop: 16 }}>
        <button onClick={() => setPage(p => Math.max(p - 1, 1))} disabled={page === 1}>
          ◀ Prev
        </button>
        <span style={{ margin: '0 12px' }}>Page {page} of {totalPages}</span>
        <button onClick={() => setPage(p => Math.min(p + 1, totalPages))} disabled={page === totalPages}>
          Next ▶
        </button>
      </div>
    </div>
  );
}
