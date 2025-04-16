import { updateOperation } from "../../utils/api";
import StatusBadge from "./StatusBadge";

export default function OperationRow({ machineId, stage, opName, status, onUpdate }) {
  const handleUpdate = async (newStatus) => {
    await updateOperation(machineId, stage, opName, newStatus);
    onUpdate(machineId, stage, opName, newStatus);
  };

  return (
    <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 6 }}>
      <div>{opName}</div>
      <div>
        <StatusBadge status={status} />
        <button onClick={() => handleUpdate("Running")}>▶ Run</button>
        <button onClick={() => handleUpdate("Success")}>✅ Verify</button>
      </div>
    </div>
  );
}
