// src/components/decommission/StageFlow.jsx
import React from "react";
import OperationDot from "./OperationDot";

export default function StageFlow({
  stageName,
  operations,
  machineId,
  onRetry,
  onCancel,
  retryMeta,
}) {
  return (
    <div className="stage-block">
      <p className="stage-title">{stageName}</p>
      <div className="operation-row">
        {Object.entries(operations).map(([op, status]) => (
          <OperationDot
            key={op}
            name={op}
            status={status}
            stage={stageName}
            machineId={machineId}
            onRetry={onRetry}
            onCancel={onCancel}
            retryMeta={retryMeta}
          />
        ))}
      </div>
    </div>
  );
}
