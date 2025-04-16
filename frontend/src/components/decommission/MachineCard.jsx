import StageFlow from "./StageFlow";

export default function MachineCard({ machine, onUpdate }) {
  return (
    <div style={{ margin: "20px 0" }}>
      <h3>{machine.name}</h3>
      {Object.entries(machine.stages).map(([stageName, stageData]) => (
        <StageFlow
          key={stageName}
          machineId={machine.id}
          stageName={stageName}
          operations={stageData.operations}
          onUpdate={onUpdate}
        />
      ))}
    </div>
  );
}
