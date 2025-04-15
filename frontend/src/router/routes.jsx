import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Decommission from '../pages/Decommission';
import Incidents from '../pages/Incidents';
import Provisioning from '../pages/Provisioning';
import Patching from '../pages/Patching';

export default function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Decommission />} />
      <Route path="/incidents" element={<Incidents />} />
      <Route path="/provisioning" element={<Provisioning />} />
      <Route path="/patching" element={<Patching />} />
    </Routes>
  );
}
