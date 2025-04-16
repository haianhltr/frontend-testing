export default function StatusBadge({ status }) {
  const emoji = {
    "Not Started": "⚪",
    "Running": "🔵",
    "Success": "🟢",
    "Failed": "🔴",
  }[status] || "❔";

  const className = {
    "Not Started": "status-not-started",
    "Running": "status-running",
    "Success": "status-success",
    "Failed": "status-failed",
  }[status];

  return <span className={`status-dot ${className}`} title={status}>{emoji}</span>;
}
