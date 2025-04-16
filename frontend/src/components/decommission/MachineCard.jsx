import React, { useState } from "react";
import StageFlow from "./StageFlow";
import "../../styles/decom.css";

export default function MachineCard({ machine }) {
  const [collapsed, setCollapsed] = useState(false);

  // Count operation statuses
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
            <StageFlow key={stage} stageName={stage} operations={data.operations} />
          ))}
        </div>
      )}
    </div>
  );
}
