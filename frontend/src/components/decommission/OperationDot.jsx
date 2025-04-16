export default function OperationDot({ machineId, stage, opName, status, onUpdate }) {
    const update = (newStatus) => {
      onUpdate(machineId, stage, opName, newStatus);
    };

    return (
      <div className="operation-dot">
        <div>● {status}</div>
        <div className="op-label">{opName}</div>
        <div className="op-buttons">
          <button onClick={() => update("Running")}>▶</button>
          <button onClick={() => update("Success")}>✔</button>
        </div>
      </div>
    );
  }
