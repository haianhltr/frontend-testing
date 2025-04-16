import React from "react";
import OperationDot from "./OperationDot";

export default function StageFlow({ stageName, operations }) {
  return (
    <div className="stage-block">
      <p className="stage-title">{stageName}</p>
      <div className="operation-row">
        {Object.entries(operations).map(([op, status]) => (
          <OperationDot key={op} name={op} status={status} />
        ))}
      </div>
    </div>
  );
}
