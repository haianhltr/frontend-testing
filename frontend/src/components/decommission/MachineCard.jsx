import React, { useState } from "react";
import StageFlow from "./StageFlow";
import { retryOperation } from "../../utils/api";
import "../../styles/decom.css";

export default function MachineCard({ machine, onUpdate }) {
  const [collapsed, setCollapsed] = useState(true);

  // 🧠 Track retrying and retryCount by stage+op
  const [retryingOps, setRetryingOps] = useState({});
  const [retryCount, setRetryCount] = useState({});

  const handleRetry = async (machineId, stage, op) => {
    const key = `${stage}-${op}`;
    if (retryingOps[key]) return;

    // 🔁 Limit retries to 3
    const count = retryCount[key] || 0;
    if (count >= 3) return;

    setRetryingOps(prev => ({ ...prev, [key]: true }));
    setRetryCount(prev => ({ ...prev, [key]: count + 1 }));

    try {
      await retryOperation(machineId, stage, op);
    } finally {
      // ♻️ Give backend time to update status
      setTimeout(() => {
        onUpdate();
        setRetryingOps(prev => ({ ...prev, [key]: false }));
      }, 1500);
    }
  };

  const handleCancelRetry = (stage, op) => {
    const key = `${stage}-${op}`;
    setRetryingOps(prev => ({ ...prev, [key]: false }));
  };

  const stageCounts = Object.values(machine.stages).flatMap(stage =>
    Object.values(stage.operations)
  );

  const statusSummary = {
    "Success": 0,
    "Running": 0,
    "Failed": 0,
    "Not Started": 0,
  };

  stageCounts.forEach(status => {
    if (statusSummary[status] !== undefined) statusSummary[status]++;
  });

  return (
    <div className="machine-card">
      <div className="machine-header" onClick={() => setCollapsed(!collapsed)}>
        <span className="machine-name">{machine.name}</span>
        <div className="machine-right">
          <div className="summary">
            🟢 {statusSummary["Success"]} | 🔄 {statusSummary["Running"]} | ❌ {statusSummary["Failed"]} | ⏳ {statusSummary["Not Started"]}
          </div>
          <button className="op-button toggle-btn">
            {collapsed ? "▶" : "🔽"}
          </button>
        </div>
      </div>

      {!collapsed && (
        <div className="machine-body">
          {Object.entries(machine.stages).map(([stage, data]) => (
            <StageFlow
              key={stage}
              stageName={stage}
              operations={data.operations}
              machineId={machine.id}
              onRetry={handleRetry}
              onCancel={handleCancelRetry}
              retryMeta={retryingOps}
            />
          ))}
        </div>
      )}
    </div>
  );
}
