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
      <p className="op-label">{name}</p>
      <div className="op-buttons">
        <button>▶</button>
        <button>✔</button>
      </div>
    </div>
  );
}
