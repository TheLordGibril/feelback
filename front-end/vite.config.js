import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',  // Garde la cible sans /api
        changeOrigin: true,  // Pour éviter les problèmes de CORS
        // Ne pas réécrire l'URL ici, donc on supprime 'rewrite'
      }
    }
  }
});
