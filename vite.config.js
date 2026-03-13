import { defineConfig } from 'vite';
import { viteSingleFile } from 'vite-plugin-singlefile';

export default defineConfig({
  plugins: [
    viteSingleFile({
      // Bundle into single HTML file
      removeConsole: false, // Keep console for debugging if needed
      removeDebugger: true,
      maxSizeInKb: 2048, // Adjust if bundle is too large
    }),
  ],
  build: {
    minify: 'esbuild',
    cssMinify: true,
    cssCodeSplit: false, // For single file
    rollupOptions: {
      output: {
        inlineDynamicImports: true,
        renderChunk: (code, chunk, options) => {
          // Ensure JS is processed for obfuscation
          return code;
        },
      },
    },
    target: 'esnext',
    sourcemap: false, // Disable sourcemaps for obfuscation
  },
});
