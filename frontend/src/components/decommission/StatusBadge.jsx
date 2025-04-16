export default function StatusBadge({ status }) {
    const emoji = {
      "Not Started": "⚪",
      "Running": "🔵",
      "Success": "🟢",
      "Failed": "🔴",
    }[status] || "❔";

    return (
      <span style={{ marginRight: 8 }}>
        {emoji} {status}
      </span>
    );
  }
