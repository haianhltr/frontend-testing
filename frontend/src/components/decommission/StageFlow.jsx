import OperationDot from "./OperationDot";

export default function StageFlow({ machineId, stageName, operations, onUpdate }) {
  return (
    <div style={{ marginBottom: "10px" }}>
      <strong>{stageName}</strong>
      <div className="operation-row">
        {Object.entries(operations).map(([opName, status]) => (
          <OperationDot
            key={opName}
            machineId={machineId}
            stage={stageName}
            opName={opName}
            status={status}
            onUpdate={onUpdate}
          />
        ))}
      </div>
    </div>
  );
}
