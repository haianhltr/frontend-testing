import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    watch: {
      usePolling: true,         // 👈 Required for Docker+Windows
      interval: 100,            // 👈 Optional: makes it snappy
    },
    host: true,                 // 👈 Required for --host flag to work in Docker
    strictPort: true,
  },
});
