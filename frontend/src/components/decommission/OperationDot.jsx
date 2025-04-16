import React from "react";

const statusIcons = {
  "Success": "✅",
  "Running": "🔄",
  "Failed": "❌",
  "Not Started": "⏳",
};

export default function OperationDot({ status, name }) {
  return (
    <div className="operation-dot" title={status}>
      <div className={`dot ${status.replace(/\s+/g, '-').toLowerCase()}`}>
        {statusIcons[status] || "❔"}
      </div>
        <p className="op-label">
          {name.replace(/_/g, " ").replace(/\b\w/g, c => c.toUpperCase())}
       </p>
      <div className="op-buttons">
        <button className="op-button" title="Run Operation">▶</button>
        <button className="op-button" title="Verify Operation">✔</button>
      </div>
    </div>
  );
}
