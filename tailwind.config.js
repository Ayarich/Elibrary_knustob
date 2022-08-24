/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [ './src_library/**/*.html'],
  theme: {
    extend: {},
  },
  plugins: [ require('flowbite/plugin')],
}
