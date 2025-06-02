/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/pages/*.{html,js,astro}",
    "./src/layouts/*.{html,js,astro}",
    "./src/components/*.{html,js,astro}",
  ],
  theme: {
    screens: {
      // 完全覆盖默认断点
      'xs': '350px',    // 折叠屏竖屏
      'sm': '480px',    // 普通手机竖屏
      'md': '680px',    // 折叠屏展开竖屏
      'lg': '960px',    // 平板/手机横屏
      'xl': '1200px',   // 平板横屏
      'xxl': '1280px'   // 桌面设备
    },
    extend: {},
  },
  plugins: [],
}

