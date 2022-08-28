/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [ './src_library/templates/*.html'],
  theme: {
    container: {
      center: true,
    },
    extend: {},
  },
  plugins: [ require('flowbite/plugin')],
}
