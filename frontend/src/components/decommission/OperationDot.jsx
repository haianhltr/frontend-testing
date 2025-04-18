import React from "react";

const statusIcons = {
  "Success": "✅",
  "Running": "🔄",
  "Failed": "❌",
  "Not Started": "⏳",
};

export default function OperationDot({
  status,
  name,
  machineId,
  stage,
  onRetry,
  onCancel,
  retryMeta = {},
}) {
  const key = `${stage}-${name}`;
  const isRetrying = retryMeta[key];

  return (
    <div className="operation-dot" title={status}>
      <div className={`dot ${status.replace(/\s+/g, '-').toLowerCase()}`}>
        {isRetrying ? "⏳" : (statusIcons[status] || "❔")}
      </div>
      <p className="op-label">
        {name.replace(/_/g, " ").replace(/\b\w/g, c => c.toUpperCase())}
      </p>
      <div className="op-buttons">
        {status === "Failed" && (
          <>
            <button
              className="op-button"
              onClick={() => onRetry(machineId, stage, name)}
              disabled={isRetrying}
            >
              {isRetrying ? "Retrying…" : "🔁 Retry"}
            </button>
            {isRetrying && (
              <button
                className="op-button cancel-button"
                onClick={() => onCancel(stage, name)}
              >
                ❌ Cancel
              </button>
            )}
          </>
        )}
      </div>
    </div>
  );
}
