// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
    site: 'https://qingke12138.top',
    // 确保GitHub Pages可以正确处理静态资源
    build: {
        assets: '_astro'
    }
});
