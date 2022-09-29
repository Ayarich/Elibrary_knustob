/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [ './src_library/templates/*.html'],
  theme: {
    container: {
      center: true,
    },
     fontFamily: {
        body: ["Erode", "serif"],
        title: ["Satoshi", "sans-serif"],
      },
    extend: {},
  },
  plugins: [ require('flowbite/plugin')],
}
