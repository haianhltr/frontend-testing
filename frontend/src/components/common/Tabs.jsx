import { Link } from 'react-router-dom';

export default function Tabs() {
  const style = { marginRight: '15px', fontWeight: 'bold' };
  return (
    <nav style={{ marginBottom: 20 }}>
      <Link to="/" style={style}>🟥 Decommission</Link>
      <Link to="/incidents" style={style}>🟢 Incidents</Link>
      <Link to="/provisioning" style={style}>🟦 Provisioning</Link>
      <Link to="/patching" style={style}>🟡 Patching</Link>
    </nav>
  );
}
