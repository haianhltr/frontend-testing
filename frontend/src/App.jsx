import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import AppRoutes from './router/routes';
import Tabs from './components/common/Tabs';

export default function App() {
  return (
    <BrowserRouter>
      <div className="container">
        <h1>⚙️ Auto-Remediation Platform</h1>
        <Tabs />
        <AppRoutes />
      </div>
    </BrowserRouter>
  );
}

